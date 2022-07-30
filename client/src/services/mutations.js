import { gql } from "@apollo/client";

export const UPDATE_BLOG_PROGRESS = gql`
  mutation updateBlogProgress(
    $userId: ID!
    $blogId: ID!
    $progressPercentage: Decimal!
  ) {
    updateBlogProgress(
      userId: $userId
      blogId: $blogId
      progressPercentage: $progressPercentage
    ) {
      ok
      message
    }
  }
`;

export const UPDATE_RESOURCE_PROGRESS = gql`
  mutation updateResourceProgress(
    $userId: ID!
    $blogId: ID!
    $resourceId: ID!
    $progressPercentage: Decimal!
  ) {
    updateResourceProgress(
      userId: $userId
      blogId: $blogId
      resourceId: $resourceId
      progressPercentage: $progressPercentage
    ) {
      ok
      message
    }
  }
`;

export const ENROLL_IN_BLOG = gql`
  mutation enrollInBlog($blogId: ID!, $userId: ID!) {
    enrollInBlog(blogId: $blogId, userId: $userId) {
      ok
      message
    }
  }
`;
