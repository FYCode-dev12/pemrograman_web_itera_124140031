import React from 'react';
import PropTypes from 'prop-types';
import './Card.css';

function Card({ children, title }) {
  return (
    <div className="custom-card">
      {title && <h3 className="custom-card-title">{title}</h3>}
      <div className="custom-card-body">{children}</div>
    </div>
  );
}

Card.propTypes = {
  children: PropTypes.node.isRequired,
  title: PropTypes.string,
};

export default Card;
