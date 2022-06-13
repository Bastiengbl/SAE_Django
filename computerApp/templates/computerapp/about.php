
<!DOCTYPE html >
<html lang="fr">

 <head> 
      {% block title %}
      <title> CONTACT</title>
      {% endblock %}
      <meta charset="utf-8">
      <meta name="viewport"
      content="width=device-width ,
      initial-scale=1">
      <!-- On ajoute un fichier CSS depuis les static -->
      {% load static %}
      <link rel="stylesheet" href="{% static 'css/style.css' %}">
      <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0-beta1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-0evHe/X+R7YkIZDRvuzKMRqM+OrBnVFBL6DOitfPri4tjfHxaWutUpFmBp4vmVor" crossorigin="anonymous">

   </head >
   <body style="background-color:#93BBEE">
    <script language="JavaScript" src="calendar.js"></script>
<script language="JavaScript">



var cal = new Calendar();
</script>
     

      {% block menu %}
      <!-- On ajoute une image depuis les static -->
      {% load static %} 
      <img src="{% static 'computerapp/images/rtdev.png' %}"
      alt="logo" style="background-color:#93BBEE;width:500px;height:200px;position:relative;left: 550px">
         {% block sidebar %} 
            
            
            <ul class="nav justify-content-center">
  <li class="nav-item">

    <a class="nav-link active" aria-current="page" href="{% url 'index' %}">Accueil</a>
  </li>
  <li class="nav-item">
    <a class="nav-link" href="{% url 'machines' %}">Machines</a>
  </li>
  <li class="nav-item">
    <a class="nav-link" href="{% url 'persos' %}">Personnel</a>
  </li>
  <li class="nav-item">
   <a class="nav-link" href="{% url 'contact' %}">Contact</a>
 </li>
 <li class="nav-item">
 <a class="nav-link" href="{% url 'infos' %}">A propos</a>
</li>
<li class="nav-item">
   <a class="nav-link" href="/admin">Administration</a>
  </li>
 
</ul>
         {% endblock %} 
      {% endblock %}
{% load static %}
<body>
<b><u>Vous pouvez contacter notre PME via les liens suivants:</u></b><br>
<br><u><br>Téléphone:</u> 06 03 97 28 96<br>
<br><u>Adresses mail:</u> <br>
<br>
<button>
<img src="/static/computerapp/images/gmail.png" width="40" height="40" alt="">
 <a href="mailto:gibelbastiengmail.com">Gmail</a> 

</button>
<button>
<img src="/static/computerapp/images/outlook.png" width="43" height="40" alt="">
<a href="mailto:fausseadressemail@outlook.com">Outlook</a><br>

</button>
<br>
<br><u>Mon compte Linkedin:</u><br>
<br>
<br>
<button>
<img src="/static/computerapp/images/linkedin.jpg" width="43" height="40" alt="">
<a href="https://fr.linkedin.com/in/bastien-gibel-2a27b6225" target="blank">Linkedin </a>
</button>
</div>

<script language="JavaScript" src="calendar.js"></script> 
<script language="JavaScript">


var cal = new Calendar();
</script>

</body>