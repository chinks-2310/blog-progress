import React from "react";
import { useMutation, useQuery } from "@apollo/client";
import { BLOG_DETAILS } from "../../services/queries";
import { Card, Spin, Row, Col, Button, message, Typography } from "antd";
import { ENROLL_IN_BLOG } from "../../services/mutations";
import { Link } from "react-router-dom";
const { Title } = Typography;

function BlogScreen() {
  const { data, loading, error } = useQuery(BLOG_DETAILS, {
    variables: { filtering: { userId: 2 } },
  });
  const [enrollInBlog] = useMutation(ENROLL_IN_BLOG, {
    onCompleted(data) {
      data?.enrollInBlog?.ok
        ? message.success(data?.enrollInBlog?.message)
        : message.error(data?.enrollInBlog?.message);
    },
    refetchQueries: [
      {
        query: BLOG_DETAILS,
        variables: { filtering: { userId: 2 } },
      },
    ],
  });
  function handleEnroll(blogId) {
    enrollInBlog({
      variables: {
        blogId: blogId,
        userId: 2,
      },
    });
  }
  if (loading) {
    return <Spin></Spin>;
  }
  if (error) {
    return <p>Error</p>;
  }
  return (
    <>
      <Title level={2}>Blogs</Title>
      <Card>
        {data?.blogDetails?.map((blogs, index) => (
          <Card key={index}>
            <Row>
              <Col span={2}>
                <Link to={{ pathname: `${blogs?.blogId}` }}>
                  {index+1}
                </Link>
              </Col>
              <Col span={12}>{blogs?.blogTitle}</Col>
              <Col span={6}>{blogs?.blogPublishedDate}</Col>
              {!blogs?.isEnrolledInBlog ? (
                <Col span={4}>
                  <Button
                    type="primary"
                    onClick={() => handleEnroll(blogs?.blogId)}
                  >
                    Enroll to View
                  </Button>
                </Col>
              ) : (
                <Col span={4}>{parseInt(blogs?.blogProgressPercentage)}%</Col>
              )}
            </Row>
          </Card>
        ))}
      </Card>
    </>
  );
}

export default BlogScreen;
