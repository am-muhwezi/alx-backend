# Queuing System in JavaScript

This project demonstrates a simple queuing system implemented in JavaScript. The system allows you to add tasks to a queue and process them in a first-in, first-out (FIFO) order.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Contributing](#contributing)
- [License](#license)

## Installation

To get started, clone the repository and install the necessary dependencies:

```bash
git clone https://github.com/yourusername/queuing-system-js.git
cd queuing-system-js
npm install
```

## Usage

Here's a basic example of how to use the queuing system:

```javascript
const Queue = require("./queue");

// Create a new queue
const queue = new Queue();

// Add tasks to the queue
queue.enqueue("Task 1");
queue.enqueue("Task 2");
queue.enqueue("Task 3");

// Process tasks
while (!queue.isEmpty()) {
  const task = queue.dequeue();
  console.log(`Processing ${task}`);
}
```

## Features

- **FIFO Order**: Tasks are processed in the order they are added.
- **Dynamic Size**: The queue can grow and shrink dynamically as tasks are added and removed.
- **Simple API**: Easy-to-use methods for adding and removing tasks.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your changes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
