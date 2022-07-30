import React from "react";
import { useQuery } from "@apollo/client";
import { BLOG_DETAILS } from "../../services/queries";
import { useParams } from "react-router-dom";
import { Spin } from "antd";
import ResourceDetails from "./components/ResourceDetails";
function ResourceScreen() {
  const { id } = useParams();
  const { data, loading, error } = useQuery(BLOG_DETAILS, {
    variables: { filtering: { userId: 2, blogId: id } },
  });
  if (loading) {
    return <Spin />;
  }
  if (error) {
    return <p>Error</p>;
  }

  return <ResourceDetails data={data} />;
}

export default ResourceScreen;
