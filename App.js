import React, { useState } from "react";
import { Checkbox, Paper, FormControlLabel, Button, TextField} from "@material-ui/core";


export default function App() {
  const [list, setList] = useState([]); //Need state for list of tasks
  const [title, setTitle] = useState("");
  const [desc, setDesc] = useState("");
  const [date, setDate] = useState(""); //Need state for the current value of each text input


  //Need a function to add a task to the task list
  const handleAdd = () => {
    setList([...list, {Title: title, Desc: desc, Date: date},]);
    setTitle("");
    setDesc("");
    setDate("");
  };

  //This is a component that will be reused to represent each individual task.
  //What props does each task need?
  const TodoItem = ({item}) => {
    //Need state to represent whether the task is checked off or not
    const [check, setCheck] = useState(false);
    //Need a function to toggle whether the task is checked off or not
    const handleCheckOff = () => {
      setCheck(!check);
    };

    const handleDelete = () => {
      setList(list.filter((i) => i !== item));
    }

    //Need a function to delete the task from the todo list
    //Note that because we've placed this component inside of our main app,
    //it has direct access to the state of our main app
    

    return (
      <Paper
        style={{
          border: "1px solid black",
          textAlign: "left",
          padding: "20px",
          minWidth: "200px",
          display: "flex",
          flexDirection: "column",
          background: "antiquewhite",
        }}
      >
        {check ? (
          <h1>
            <strike>{item.Title}</strike>
          </h1>
        ) : (
          <>
            <h1 style={{ margin: 0 }}>{item.Title}</h1>
            <p style={{ margin: 5 }}>{item.Desc}</p>
            <p style={{ margin: 5 }}>Due: {item.Date}</p>
          </>
        )}
        ​<FormControlLabel
          control={<Checkbox value="checkedA" label="Check off" onClick={handleCheckOff} style={{ marginBottom: "10px" }} />}
          label="Check off"
        />
        <Button variant="contained" onClick={handleDelete}>Delete</Button>
      </Paper>
    );
  };
  return (
    <div
      style={{ display: "flex", flexDirection: "column", alignItems: "center" }}
    >
      <div style={{ display: "flex", flexDirection: "column", width: "300px" }}>
        <label style={{ marginBottom: "10px" }}>
          {"Title: "}
          <TextField id="outlined-basic" label="Name of task" variant="outlined"
            value={title}
            onChange={(e) => setTitle(e.target.value)}
          />
        </label>
        <label style={{ marginBottom: "10px" }}>
          {"Description: "}
          <TextField id="outlined-basic" label="Description of task" variant="outlined"
            value={desc}
            onChange={(e) => setDesc(e.target.value)}
          />
        </label>
        <label style={{ marginBottom: "10px" }}>
          {"Due Date: "}
          <TextField id="outlined-basic" label="Due date of task" variant="outlined"
            value={date}
            onChange={(e) => setDate(e.target.value)}
          />
        </label>
      </div>
      <Button variant="contained" color="primary" onClick={handleAdd} style={{ marginBottom: "20px" }}>
        Add Todo Item
      </Button>
      ​
      {list.map((item) => (
        <TodoItem item={item} />
      ))}
    </div>
  );
}
