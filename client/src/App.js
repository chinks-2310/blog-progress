import React from "react";
import "./App.css";
import { Layout } from "antd";
import SideBar from "./components/SideBar";
import RoutesPage from "./config/Routes";
const { Content } = Layout;

function App() {
  return (
    <Layout style={{ minHeight: "100vh" }}>
      <SideBar />
      <Layout>
        <Content className="app-content">
          <RoutesPage />
        </Content>
      </Layout>
    </Layout>
  );
}

export default App;
