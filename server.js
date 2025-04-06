Welcome to Node.js v22.11.0.
Type ".help" for more information.
> const express = require('express');
Uncaught Error: Cannot find module 'express'
Require stack:
- <repl>
    at Function._resolveFilename (node:internal/modules/cjs/loader:1249:15)
    at Function._load (node:internal/modules/cjs/loader:1075:27)
    at TracingChannel.traceSync (node:diagnostics_channel:315:14)
    at wrapModuleLoad (node:internal/modules/cjs/loader:218:24)
    at Module.require (node:internal/modules/cjs/loader:1340:12)
    at require (node:internal/modules/helpers:141:16) {
  code: 'MODULE_NOT_FOUND',
  requireStack: [ '<repl>' ]
}
> const multer = require('multer');
Uncaught Error: Cannot find module 'multer'
Require stack:
- <repl>
    at Function._resolveFilename (node:internal/modules/cjs/loader:1249:15)
    at Function._load (node:internal/modules/cjs/loader:1075:27)
    at TracingChannel.traceSync (node:diagnostics_channel:315:14)
    at wrapModuleLoad (node:internal/modules/cjs/loader:218:24)
    at Module.require (node:internal/modules/cjs/loader:1340:12)
    at require (node:internal/modules/helpers:141:16) {
  code: 'MODULE_NOT_FOUND',
  requireStack: [ '<repl>' ]
}
> const path = require('path');
undefined
> const app = express();
Uncaught ReferenceError: express is not defined
>
> // Set up storage for uploaded files
undefined
> const storage = multer.diskStorage({
...     destination: './uploads/',
...     filename: (req, file, cb) => {
...         cb(null, file.fieldname + '-' + Date.now() + path.extname(file.originalname));
...     }
... });
Uncaught ReferenceError: multer is not defined
> const upload = multer({ storage });
Uncaught ReferenceError: multer is not defined
>
> // Serve static files (your HTML, CSS, JS)
undefined
> app.use(express.static(__dirname));
Uncaught ReferenceError: app is not defined
> app.use(express.json());
Uncaught ReferenceError: app is not defined
> app.use(express.urlencoded({ extended: true }));
Uncaught ReferenceError: app is not defined
>
> // Handle the post creation route
undefined
> app.post('/eh/create_eh_post', upload.single('media'), (req, res) => {
...     const content = req.body.content;
...     const media = req.file ? req.file.filename : null;
...     console.log('New Post:', { content, media });
...     res.redirect('/EH.html'); // Redirect back to EH.html after posting
... });
Uncaught ReferenceError: app is not defined
>
> // Start the server
undefined
> const PORT = 3000;
undefined
> app.listen(PORT, () => {
...     console.log(`Server running on http://localhost:${PORT}`);
... });Open a terminal in your project directory.
