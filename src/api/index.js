import axios from "axios";

const api = axios.create({
  headers: {
    "Content-Type": "application/json",
    "X-CSRF-TOKEN": document
      .querySelector('meta[name="csrf-token"]')
      .getAttribute("content"),
  },
});

export default {
  
};
