import React from "react";
// import ReactDOM from "react-dom";
import MDEditor from '@uiw/react-md-editor';

function App() {
  const [value, setValue] = React.useState("Please __Enter__ ~~your~~ **words**.(预览用)");
  return (
    <div className="container">
      <MDEditor
        value={value}
        // onChange={setValue}
      />
    </div>
  );
}

export default App;
