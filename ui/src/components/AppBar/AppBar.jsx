import React from 'react';
import { NavLink } from 'react-router-dom';

export const AppBar = () => {
  return (
    <header>
      <nav style={{ display: 'flex', gap: '15px' }}>
        <NavLink to="/">Home</NavLink>
        <NavLink to="/myapp">MyApp</NavLink>
      </nav>
    </header>
  );
};
