import { gql } from "@apollo/client";

export const BLOG_PROGRESS_FOR_USER = gql`
  query blogProgress($filtering: BlogProgressForUserInput) {
    blogProgress(filtering: $filtering) {
      blogId
      blogTitle
      blogStatus
      blogProgressPercentage
      resources {
        resourceId
        resourceType
        resourceLink
        resourceText
        resourceStatus
        resourceProgressPercentage
      }
    }
  }
`;

export const BLOG_DETAILS = gql`
  query blogDetails($filtering: BlogsForUserInput!) {
    blogDetails(filtering: $filtering) {
      blogId
      blogTitle
      blogPublishedDate
      isEnrolledInBlog
      blogProgressPercentage
      resources {
        resourceId
        resourceType
        resourceLink
        resourceText
        resourceProgressPercentage
      }
    }
  }
`;
