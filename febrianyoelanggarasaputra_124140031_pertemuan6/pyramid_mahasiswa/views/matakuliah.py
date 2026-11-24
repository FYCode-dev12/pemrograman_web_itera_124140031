from pyramid.view import view_config
from pyramid.httpexceptions import (
    HTTPNotFound,
    HTTPBadRequest,
)
from ..models import Matakuliah


# 1. READ ALL: Menampilkan seluruh daftar mata kuliah
@view_config(route_name='matakuliah_list', renderer='json')
def matakuliah_list(request):
    """View untuk mengambil semua data mata kuliah"""
    dbsession = request.dbsession
    matakuliah_all = dbsession.query(Matakuliah).order_by(Matakuliah.id.asc()).all()
    return {'matakuliah': [m.to_dict() for m in matakuliah_all]}


# 2. READ ONE: Menampilkan detail mata kuliah berdasarkan ID
@view_config(route_name='matakuliah_detail', renderer='json')
def matakuliah_detail(request):
    """View untuk melihat detail satu mata kuliah berdasarkan ID"""
    dbsession = request.dbsession
    mk_id = request.matchdict['id']

    try:
        mk_id_int = int(mk_id)
    except ValueError:
        return HTTPNotFound(json_body={'error': f'Matakuliah dengan ID {mk_id} tidak ditemukan'})

    matakuliah = dbsession.query(Matakuliah).filter_by(id=mk_id_int).first()
    if matakuliah is None:
        return HTTPNotFound(json_body={'error': f'Matakuliah dengan ID {mk_id} tidak ditemukan'})

    return {'matakuliah': matakuliah.to_dict()}


# 3. CREATE: Menambahkan data mata kuliah baru
@view_config(route_name='matakuliah_add', request_method='POST', renderer='json')
def matakuliah_add(request):
    """View untuk menambahkan mata kuliah baru dari payload JSON"""
    try:
        json_data = request.json_body
    except Exception:
        return HTTPBadRequest(json_body={'error': 'Payload request harus berupa JSON yang valid'})

    # Validasi field wajib: kode_mk, nama_mk, sks, semester
    required_fields = ['kode_mk', 'nama_mk', 'sks', 'semester']
    for field in required_fields:
        if field not in json_data or json_data[field] is None or json_data[field] == '':
            return HTTPBadRequest(json_body={'error': f'Field {field} wajib diisi!'})

    # Validasi sks dan semester bertipe integer dan bernilai positif (> 0)
    try:
        sks = int(json_data['sks'])
        if sks <= 0:
            return HTTPBadRequest(json_body={'error': 'Nilai SKS harus berupa integer positif lebih dari 0'})
    except (ValueError, TypeError):
        return HTTPBadRequest(json_body={'error': 'Nilai SKS harus berupa angka integer valid'})

    try:
        semester = int(json_data['semester'])
        if semester <= 0:
            return HTTPBadRequest(json_body={'error': 'Nilai Semester harus berupa integer positif lebih dari 0'})
    except (ValueError, TypeError):
        return HTTPBadRequest(json_body={'error': 'Nilai Semester harus berupa angka integer valid'})

    dbsession = request.dbsession

    # Validasi keunikan kode_mk
    kode_mk_val = str(json_data['kode_mk']).strip()
    existing = dbsession.query(Matakuliah).filter_by(kode_mk=kode_mk_val).first()
    if existing:
        return HTTPBadRequest(json_body={'error': f"Kode matakuliah '{kode_mk_val}' sudah terdaftar!"})

    nama_mk_val = str(json_data['nama_mk']).strip()
    if not nama_mk_val:
        return HTTPBadRequest(json_body={'error': 'Field nama_mk tidak boleh kosong!'})

    matakuliah = Matakuliah(
        kode_mk=kode_mk_val,
        nama_mk=nama_mk_val,
        sks=sks,
        semester=semester
    )

    dbsession.add(matakuliah)
    dbsession.flush()

    return {'success': True, 'matakuliah': matakuliah.to_dict()}


# 4. UPDATE: Memperbarui data mata kuliah yang ada
@view_config(route_name='matakuliah_update', request_method='PUT', renderer='json')
def matakuliah_update(request):
    """View untuk mengupdate data mata kuliah berdasarkan ID"""
    dbsession = request.dbsession
    mk_id = request.matchdict['id']

    try:
        mk_id_int = int(mk_id)
    except ValueError:
        return HTTPNotFound(json_body={'error': f'Matakuliah dengan ID {mk_id} tidak ditemukan'})

    matakuliah = dbsession.query(Matakuliah).filter_by(id=mk_id_int).first()
    if matakuliah is None:
        return HTTPNotFound(json_body={'error': f'Matakuliah dengan ID {mk_id} tidak ditemukan'})

    try:
        json_data = request.json_body
    except Exception:
        return HTTPBadRequest(json_body={'error': 'Payload request harus berupa JSON yang valid'})

    # Update kode_mk jika disertakan
    if 'kode_mk' in json_data and json_data['kode_mk']:
        new_kode = str(json_data['kode_mk']).strip()
        if new_kode != matakuliah.kode_mk:
            existing = dbsession.query(Matakuliah).filter_by(kode_mk=new_kode).first()
            if existing:
                return HTTPBadRequest(json_body={'error': f"Kode matakuliah '{new_kode}' sudah digunakan!"})
            matakuliah.kode_mk = new_kode

    # Update nama_mk jika disertakan
    if 'nama_mk' in json_data:
        new_nama = str(json_data['nama_mk']).strip()
        if not new_nama:
            return HTTPBadRequest(json_body={'error': 'Field nama_mk tidak boleh kosong!'})
        matakuliah.nama_mk = new_nama

    # Update sks jika disertakan
    if 'sks' in json_data and json_data['sks'] is not None:
        try:
            sks = int(json_data['sks'])
            if sks <= 0:
                return HTTPBadRequest(json_body={'error': 'Nilai SKS harus berupa integer positif lebih dari 0'})
            matakuliah.sks = sks
        except (ValueError, TypeError):
            return HTTPBadRequest(json_body={'error': 'Nilai SKS harus berupa angka integer valid'})

    # Update semester jika disertakan
    if 'semester' in json_data and json_data['semester'] is not None:
        try:
            semester = int(json_data['semester'])
            if semester <= 0:
                return HTTPBadRequest(json_body={'error': 'Nilai Semester harus berupa integer positif lebih dari 0'})
            matakuliah.semester = semester
        except (ValueError, TypeError):
            return HTTPBadRequest(json_body={'error': 'Nilai Semester harus berupa angka integer valid'})

    return {'success': True, 'matakuliah': matakuliah.to_dict()}


# 5. DELETE: Menghapus data mata kuliah berdasarkan ID
@view_config(route_name='matakuliah_delete', request_method='DELETE', renderer='json')
def matakuliah_delete(request):
    """View untuk menghapus mata kuliah berdasarkan ID"""
    dbsession = request.dbsession
    mk_id = request.matchdict['id']

    try:
        mk_id_int = int(mk_id)
    except ValueError:
        return HTTPNotFound(json_body={'error': f'Matakuliah dengan ID {mk_id} tidak ditemukan'})

    matakuliah = dbsession.query(Matakuliah).filter_by(id=mk_id_int).first()
    if matakuliah is None:
        return HTTPNotFound(json_body={'error': f'Matakuliah dengan ID {mk_id} tidak ditemukan'})

    dbsession.delete(matakuliah)

    return {'success': True, 'message': f'Matakuliah dengan ID {mk_id} berhasil dihapus'}
