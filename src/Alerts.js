import Alert from 'react-bootstrap/Alert';
import Button from 'react-bootstrap/Button';
import React, {useState} from "react"
import '../node_modules/bootstrap/dist/css/bootstrap.min.css';

function Alerts() {
    // const [show, setShow] = useState(true);
    // return (
    //     <>
    //     <Alert show={show} variant="success">

    //         <Alert.Heading>Hey, it's markdown preview part</Alert.Heading>
    //         <p>这是一个占位组件，用于之后的填充以及布局设计</p>
    //         <hr />
    //         <div className="d-flex justify-content-end">
    //             <Button onClick={() => setShow(false)} variant="outline-success">
    //                点击以关闭
    //       </Button>
    //         </div>
    //     </Alert>
    //     {!show && <Button onClick={() => setShow(true)}>点击以重新打开</Button>}
    //     </>
    // );
    const [show, setShow] = useState(true);

    return (
      <>
        <Alert color='primary' show={show} variant="success">
          <Alert.Heading>How's it going?!</Alert.Heading>
          <p>
            Duis mollis, est non commodo luctus, nisi erat porttitor ligula, eget
            lacinia odio sem nec elit. Cras mattis consectetur purus sit amet
            fermentum.
          </p>
          <hr />
          <div className="d-flex justify-content-end">
            <Button onClick={() => setShow(false)} variant="outline-success">
              Close me y'all!
            </Button>
          </div>
        </Alert>
  
        {!show && <Button onClick={() => setShow(true)}>Show Alert</Button>}
      </>
    );
}

export default Alerts;
