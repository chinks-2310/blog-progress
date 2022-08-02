import React from 'react'
import { useMutation } from "@apollo/client";
import { Button, Row, Col, Card } from 'antd';
import { useState } from 'react';
import { message } from 'antd';
import { CheckCircleFilled, CheckCircleOutlined } from '@ant-design/icons'
import './styles.css'
import { UPDATE_RESOURCE_PROGRESS } from '../../services/mutations';
import { BLOG_DETAILS } from '../../services/queries';
import VideoComponent from '../VideoComponent';
import ModalToPreviewFiles from '../../views/PdfViewer';
const renderResource = (resource, disable) => {
    switch (resource?.resourceType) {
        case 'Image':
            return <div className='resource'><img src={resource?.resourceLink} alt="resource-img"></img></div>

        case 'Video':
            return(
              <VideoComponent disable={disable} resourceLink={resource?.resourceLink}/>
            )

        case 'PDF':
            return <ModalToPreviewFiles disable={disable} fileLink={resource?.resourceLink}/>

        case 'Text':
            return <div dangerouslySetInnerHTML={{ __html: resource.resourceText }}></div>

        default:
            return <div />
    }
}

const ResourceTemplate = ({ resource, disabled, blogId }) => {
    const [loading, setLoading] = useState(false);

    const [markResourceAsDone] = useMutation(UPDATE_RESOURCE_PROGRESS, {
        onCompleted(data) {
          setLoading(false);
          data?.updateResourceProgress?.ok
            ? message.success(data?.updateResourceProgress?.message)
            : message.error(data?.updateResourceProgress?.message);
        },
        refetchQueries: [
          {
            query: BLOG_DETAILS,
            variables: { filtering: { blogId: blogId, userId: 2 } },
          },
        ],
      });

    const markAsDone = () => {
        setLoading(true)
        markResourceAsDone({
            variables: {
              blogId: blogId,
              userId: 2,
              resourceId:resource?.resourceId,
              progressPercentage: parseFloat(100)
            },
          });
    }
    return (
        <Row style={{ margin: '50px 0px' }}>
            <Col md={2}>
                <Button
                    type={resource?.resourceProgressPercentage !== parseFloat(100) && "default"}
                    className={resource?.resourceProgressPercentage === parseFloat(100) ? 'button button__success' : 'button'}
                    onClick={markAsDone}
                    loading={loading}
                    icon={resource?.resourceProgressPercentage === "100.00" ? <CheckCircleFilled /> : <CheckCircleOutlined />}
                    disabled={resource?.resourceProgressPercentage === "100.00" || disabled}
                />
            </Col>
            <Col md={22}>
              <Card>
                {renderResource(resource, disabled)}
              </Card>
            </Col>
        </Row>
    )
}

export default ResourceTemplate 
