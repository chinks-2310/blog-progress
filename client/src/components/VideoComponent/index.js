import React from 'react'

function VideoComponent({disable, resourceLink}) {
  return (
        <div className={disable && 'resource'}><iframe width="560" height="315" src={resourceLink}
            title="YouTube video player" frameBorder="0"
            allow="accelerometer; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
            allowFullScreen></iframe>
        </div>
  )
}

export default VideoComponent