import React from "react";

const ModalToPreviewFiles = ({fileLink, disable}) => {
  return (
    <>
        <div className={disable && 'resource'}>
            <iframe
                src={`${fileLink}`}
                title="PDF Viewer"
                width="850"
                height="600"
            ></iframe>
        </div>
    </>
  );

};

 

export default ModalToPreviewFiles;