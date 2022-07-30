import React, { useState } from "react";
import { Layout, Menu } from "antd";
import { DesktopOutlined } from "@ant-design/icons";
const { Sider } = Layout;

function SideBar() {
  const [collapsed, setCollapsed] = useState(false);
  return (
    <Sider
      collapsible
      collapsed={collapsed}
      onCollapse={(value) => setCollapsed(value)}
    >
      <Menu theme="dark" defaultSelectedKeys={["1"]} mode="inline">
        <Menu.Item key={1} icon={<DesktopOutlined />}>
          Blogs
        </Menu.Item>
      </Menu>
    </Sider>
  );
}

export default SideBar;
