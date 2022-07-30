import { Card, Row, Col, Button, Alert } from "antd";
import React from "react";

function ResourceDetails({ data }) {
  return (
    <>
      {!data?.blogDetails[0]?.isEnrolledInBlog && (
        <Alert
          type="info"
          description="Please Enroll in Blog to view Resources"
        />
      )}
      <Card>
        {data?.blogDetails[0]?.resources?.map((resource) => (
          <Card>
            <Row>
              <Col span={2}>{resource?.resourceId}</Col>
              <Col span={4}>{resource?.resourceType}</Col>
              <Col span={10}>{resource?.resourceLink}</Col>
              <Col span={4}>
                <Button
                  type="primary"
                  disabled={!data?.blogDetails[0]?.isEnrolledInBlog}
                >
                  Open
                </Button>
              </Col>
              {data?.blogDetails[0]?.isEnrolledInBlog && (
                <Col span={4}>
                  {parseInt(resource?.resourceProgressPercentage)}%
                </Col>
              )}
            </Row>
          </Card>
        ))}
      </Card>
    </>
  );
}

export default ResourceDetails;
