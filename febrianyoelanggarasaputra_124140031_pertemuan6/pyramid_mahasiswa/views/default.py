from pyramid.view import view_config


@view_config(route_name='home', renderer='json')
def home_view(request):
    """View selamat datang di root API"""
    return {
        'status': 'success',
        'message': 'Selamat datang di RESTful API Pyramid Mahasiswa & Matakuliah',
        'praktikan': {
            'nama': 'Febrian Yoel Anggara Saputra',
            'nim': '124140031',
            'kelas': 'RB'
        },
        'endpoints': {
            'mahasiswa': '/api/mahasiswa',
            'matakuliah': '/api/matakuliah'
        }
    }
