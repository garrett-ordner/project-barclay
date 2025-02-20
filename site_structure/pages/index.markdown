---
layout: default
title: Project Barclay
---


<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Project Barclay</title>
    <link rel="icon" type="image/x-icon" href="favicon.ico">
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f4;
            margin: 0;
            padding: 0;
        }
        .header {
            background-color: #2c3e50;
            color: #ffffff;
            padding: 20px;
            text-align: center;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }
        .header h1 {
            margin: 0;
            font-size: 32px;
        }
        .content {
            padding: 20px;
        }
        .book-list {
            list-style-type: none;
            padding: 0;
        }
        .book-list li {
            margin: 10px 0;
        }
        .book-list a {
            text-decoration: none;
            color: #0073e6;
            font-size: 18px;
            display: block;
            padding: 8px;
            border-radius: 4px;
            transition: background-color 0.2s;
        }
        .book-list a:hover {
            text-decoration: underline;
            background-color: rgba(0, 115, 230, 0.1);
        }
        @media (max-width: 600px) {
            .header h1 {
                font-size: 24px;
            }
            .book-list a {
                font-size: 16px;
            }
        }
    </style>
</head>
<body>
    <div class="header">
        <h1>Project Barclay Book Repository</h1>
    </div>
    <div class="content">
        <p>Download the latest versions:</p>
        <ul class="book-list">
            <li>
                <a href="https://github.com/garrett-ordner/project-barclay/releases/latest/download/barclay-catechism-thought-for-thought.pdf"
                   target="_blank"
                   download>
                    Barclay's Catechism (Thought-for-Thought)
                </a>
            </li>
            <li>
                <a href="https://github.com/garrett-ordner/project-barclay/releases/latest/download/barclay-confession-thought-for-thought.pdf"
                   target="_blank"
                   download>
                    Barclay's Confession (Thought-for-Thought)
                </a>
            </li>
        </ul>
    </div>
</body>
</html>
