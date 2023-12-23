import React, { lazy } from 'react';
import { Route, Routes } from 'react-router-dom';
import { Layout } from './Layout';

const Home = lazy(() => import('../pages/Home'));
const MyApp = lazy(() => import('../pages/MyApp'));

export const App = () => {
  return (
    <Routes>
      <Route path="/" element={<Layout />}>
        <Route index element={<Home />} />
        <Route path="myapp" element={<MyApp />} />
        <Route path="*" element={<div>Page not found</div>} />
      </Route>
    </Routes>
  );
};
