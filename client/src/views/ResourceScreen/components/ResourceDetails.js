import { Alert, Progress, Typography, Button, message, Row, Col } from "antd";
import React from "react";
import { useMutation } from "@apollo/client";
import { ENROLL_IN_BLOG } from "../../../services/mutations";
import ResourceTemplate from "../../../components/ResourceTemplate";
import { BLOG_DETAILS } from "../../../services/queries";
const { Title } = Typography;

function ResourceDetails({ data }) {
  const [enrollInBlog] = useMutation(ENROLL_IN_BLOG, {
    onCompleted(data) {
      data?.enrollInBlog?.ok
        ? message.success(data?.enrollInBlog?.message)
        : message.error(data?.enrollInBlog?.message);
    },
    refetchQueries: [
      {
        query: BLOG_DETAILS,
        variables: { filtering: { userId: 2, blogId: data?.blogDetails[0]?.blogId  } },
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
  return (
    <>
    <Title level={2}>Resources</Title>
      {!data?.blogDetails[0]?.isEnrolledInBlog && (
        <Alert
          type="info"
          description={
          <Row>
            <Col span={8}>Please Enroll in Blog to view Resources</Col>
            <Col span={8}></Col>
            <Col span={8} style={{display: 'flex', justifyContent: 'flex-end'}}>          
              <Button
              type="primary"
              onClick={() => handleEnroll(data?.blogDetails[0]?.blogId)}
              >
              Enroll to View
              </Button>
            </Col>
          </Row>}
        >
        </Alert>
      )}

      {data?.blogDetails[0]?.isEnrolledInBlog && (<Progress
        style={{ top: '0px', width: '70vw' }}
        percent={data?.blogDetails[0]?.blogProgressPercentage}
        status="active"
      />)}

      {data?.blogDetails[0]?.resources?.map((resource) => <ResourceTemplate resource={resource} disabled={!data?.blogDetails[0]?.isEnrolledInBlog} blogId={data?.blogDetails[0]?.blogId} />)}
    </>
  );
}

export default ResourceDetails;