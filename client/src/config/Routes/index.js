import React from "react";
import { Routes, Route } from "react-router-dom";
import BlogScreen from "../../views/BlogScreen";
import ResourceScreen from "../../views/ResourceScreen";

const RoutesPage = () => {
  return (
    <Routes>
      <Route path="/" element={<BlogScreen />} />
      <Route path={"/:id"} element={<ResourceScreen />} />
    </Routes>
  );
};
export default RoutesPage;
