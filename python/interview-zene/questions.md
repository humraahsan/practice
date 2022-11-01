## What is FAST API?
- high performant web framework for building backend APIs with python 3.7 and above
- light weighted than django and flask
- way of defining routes is similar to flask

## What is React?
- Declarative, efficient & flexible JS Library for building fast and interactive UI
- component based architecture.
- component is implemented as JS class that has a state and a render method
- state contains the data that we want to display when the component is rendered
- render method is responsible for describing what the UI should look like

### Consuming API in react front end

Using `fetch()`
```javascript
// Using fetch()

const url = "https://jsonplaceholder.typicode.com/todos";
const options = {
  method: "POST", // < -- difference
  headers: {
    Accept: "application/json",
    "Content-Type": "application/json;charset=UTF-8",
  },
  body: JSON.stringify({
    a: 10,
    b: 20,
  }),
};
fetch(url, options)
  .then((response) => response.json())
  .then((data) => {
    console.log(data);
  });
```

Using `axios`
```javascript
const url = 'https://jsonplaceholder.typicode.com/posts'
const data = {
  a: 10,
  b: 20,
};
axios
  .post(url, data, {
    headers: {
      Accept: "application/json",
      "Content-Type": "application/json;charset=UTF-8",
    },
  })
  .then(({data}) => {
    console.log(data);
});
```
- Axios automatically does JSON data transformation, can set timeouts easily, can put interceptor on HTTP requests
