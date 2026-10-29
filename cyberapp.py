from pathlib import Path

html = r'''<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>CyberLab Pro — Apprendre la cybersécurité</title>
<style>
:root{--bg:#080d18;--panel:#101a2b;--panel2:#152238;--line:#273750;--text:#edf4ff;--muted:#a3b4ce;--cyan:#5eead4;--blue:#60a5fa;--green:#86efac;--orange:#fbbf24;--red:#fda4af}
*{box-sizing:border-box}body{margin:0;background:radial-gradient(ellipse at top,#13243b 0,#080d18 52%);color:var(--text);font:15px/1.55 system-ui,-apple-system,Segoe UI,sans-serif}button,input,select{font:inherit}button{cursor:pointer;border:1px solid var(--line);background:#1b2a42;color:var(--text);padding:10px 14px;border-radius:10px;font-weight:650}button:hover{border-color:var(--cyan);transform:translateY(-1px)}button.primary{background:var(--cyan);color:#06201e;border-color:transparent}button.ghost{background:transparent}.app{max-width:1250px;margin:auto;padding:22px}.top{display:flex;align-items:center;justify-content:space-between;gap:16px;margin-bottom:22px}.brand{display:flex;gap:12px;align-items:center}.logo{width:48px;height:48px;border-radius:14px;background:linear-gradient(135deg,#5eead4,#60a5fa);display:grid;place-items:center;color:#061323;font-size:25px;font-weight:900}.brand h1{font-size:21px;margin:0}.brand p{margin:2px 0 0;color:var(--muted);font-size:13px}.pill{border:1px solid var(--line);border-radius:99px;padding:7px 11px;color:var(--muted);font-size:12px}.layout{display:grid;grid-template-columns:245px minmax(0,1fr);gap:20px}.sidebar,.panel,.hero{background:rgba(16,26,43,.94);border:1px solid var(--line);border-radius:18px}.sidebar{padding:12px;height:max-content;position:sticky;top:12px}.navbtn{width:100%;text-align:left;background:transparent;border-color:transparent;color:var(--muted);display:flex;align-items:center;gap:10px;margin:3px 0}.navbtn.active{background:#1b3045;color:var(--cyan);border-color:#2d5360}.navbtn span:first-child{font-size:18px;width:24px;text-align:center}.sidefoot{border-top:1px solid var(--line);margin-top:12px;padding:15px 8px 5px;color:var(--muted);font-size:12px}.main{min-width:0}.hero{padding:26px;margin-bottom:18px;background:linear-gradient(120deg,rgba(20,49,66,.95),rgba(16,26,43,.96))}.eyebrow{font-size:11px;color:var(--cyan);letter-spacing:1.5px;text-transform:uppercase;font-weight:800}.hero h2{font-size:clamp(25px,4vw,37px);line-height:1.15;margin:8px 0 10px;max-width:700px}.hero p{color:var(--muted);max-width:700px;margin:0 0 17px}.stats{display:grid;grid-template-columns:repeat(3,1fr);gap:10px;margin-top:20px}.stat{background:rgba(6,13,25,.38);border:1px solid var(--line);border-radius:12px;padding:13px}.stat strong{display:block;font-size:22px}.stat small{color:var(--muted)}.cards{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:13px}.panel{padding:19px;margin-bottom:15px}.module{display:flex;gap:13px;align-items:flex-start}.modicon{width:43px;height:43px;flex:0 0 43px;display:grid;place-items:center;border-radius:12px;background:#1b3045;font-size:21px}.module h3{margin:0 0 4px;font-size:16px}.module p{margin:0;color:var(--muted);font-size:13px}.meta{display:flex;gap:8px;flex-wrap:wrap;margin:13px 0;color:var(--muted);font-size:12px}.meta span{background:#0a1423;border:1px solid var(--line);padding:4px 8px;border-radius:99px}.module button{width:100%;margin-top:7px}.sectionhead{display:flex;align-items:flex-end;justify-content:space-between;gap:12px;margin:24px 0 12px}.sectionhead h2{margin:0;font-size:21px}.sectionhead p{margin:4px 0 0;color:var(--muted);font-size:13px}.progress{height:8px;background:#25344a;border-radius:99px;overflow:hidden;margin-top:9px}.progress i{display:block;height:100%;background:linear-gradient(90deg,var(--cyan),var(--blue));width:0}.lesson h2{margin-top:0}.lesson h3{margin:20px 0 6px}.lesson p,.lesson li{color:#c7d4e8}.lesson code,.terminal code{background:#07101d;border:1px solid var(--line);padding:2px 5px;border-radius:5px;color:var(--cyan)}.callout{background:#102b2c;border:1px solid #245754;border-radius:12px;padding:13px;margin:15px 0}.warning{background:#302616;border-color:#6a4e1c}.quizq{border-top:1px solid var(--line);padding:14px 0}.quizq:first-child{border-top:0}.quizq p{font-weight:700;margin:0 0 9px}.choice{display:block;width:100%;text-align:left;margin:7px 0;background:#0b1525;font-weight:500}.choice.correct{border-color:#4ade80;color:#bbf7d0}.choice.wrong{border-color:#fb7185;color:#fecdd3}.terminal{background:#050a11;border:1px solid #31425a;border-radius:14px;overflow:hidden}.termbar{background:#111d2e;padding:10px 14px;display:flex;justify-content:space-between;align-items:center;color:var(--muted);font-size:12px}.dots{display:flex;gap:5px}.dots i{width:8px;height:8px;background:#64748b;border-radius:50%}.termout{padding:15px;min-height:220px;max-height:340px;overflow:auto;font:13px/1.7 ui-monospace,SFMono-Regular,Consolas,monospace;white-space:pre-wrap;color:#cbd5e1}.termout .good{color:var(--green)}.termout .info{color:var(--cyan)}.termout .warn{color:var(--orange)}.termout .bad{color:var(--red)}.termform{display:flex;gap:8px;border-top:1px solid #1d2b3d;padding:11px}.termform input{min-width:0;flex:1;background:#0b1422;border:1px solid #31425a;border-radius:8px;padding:10px;color:var(--text);font-family:monospace;outline:none}.termform input:focus{border-color:var(--cyan)}.hint{color:var(--muted);font-size:12px;margin-top:9px}.challenge{border:1px solid var(--line);background:#0b1525;border-radius:13px;padding:15px;margin:10px 0}.challenge h3{margin:0 0 5px}.challenge p{margin:0 0 12px;color:var(--muted)}.badgegrid{display:grid;grid-template-columns:repeat(3,1fr);gap:10px}.badgecard{border:1px solid var(--line);border-radius:12px;padding:14px;text-align:center;background:#0b1525}.badgecard .big{font-size:25px}.badgecard small{display:block;color:var(--muted)}.badgecard.locked{opacity:.45;filter:grayscale(1)}.glossary{display:grid;grid-template-columns:repeat(2,1fr);gap:10px}.term{border:1px solid var(--line);border-radius:10px;padding:12px}.term strong{color:var(--cyan)}.term p{color:var(--muted);margin:4px 0 0;font-size:13px}.hidden{display:none!important}.notice{color:var(--muted);font-size:12px;margin-top:18px}.toast{padding:11px;border-radius:10px;background:#12312d;border:1px solid #2b6a5d;color:#c8fff1;margin:10px 0}.footer{margin:22px 0;color:#71839e;font-size:12px;text-align:center}
@media(max-width:850px){.layout{grid-template-columns:1fr}.sidebar{position:static;display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:3px}.sidefoot{grid-column:1/-1}.cards{grid-template-columns:1fr}.top{align-items:flex-start}.stats{grid-template-columns:repeat(3,1fr)}}@media(max-width:520px){.app{padding:12px}.top{flex-direction:column}.hero{padding:20px}.sidebar{grid-template-columns:1fr 1fr}.navbtn{font-size:12px;padding:8px}.stats{gap:6px}.stat{padding:9px}.stat strong{font-size:18px}.glossary,.badgegrid{grid-template-columns:1fr}.termform button{padding:9px}}
</style>
</head>
<body>
<div class="app">
<header class="top">
  <div class="brand"><div class="logo">⌘</div><div><h1>CyberLab <span style="color:var(--cyan)">PRO</span></h1><p>Ton laboratoire de cybersécurité éthique</p></div></div>
  <div class="pill">● Mode local · Entraînement sécurisé</div>
</header>
<div class="layout">
<aside class="sidebar" aria-label="Navigation">
  <button class="navbtn active" data-page="home"><span>⌂</span> Tableau de bord</button>
  <button class="navbtn" data-page="learn"><span>▤</span> Parcours & cours</button>
  <button class="navbtn" data-page="terminal"><span>⌘</span> Terminal Linux</button>
  <button class="navbtn" data-page="challenges"><span>⚑</span> Défis pratiques</button>
  <button class="navbtn" data-page="quiz"><span>✓</span> Quiz de sécurité</button>
  <button class="navbtn" data-page="badges"><span>✦</span> Mes badges</button>
  <button class="navbtn" data-page="glossary"><span>⌕</span> Glossaire</button>
  <div class="sidefoot">Tout se passe dans ce navigateur. Le terminal est simulé : aucune commande n'est exécutée sur ton ordinateur ni sur Internet.</div>
</aside>
<main class="main">
<section id="page-home" class="page">
  <div class="hero"><div class="eyebrow">Formation interactive · Niveau débutant → intermédiaire</div><h2>Comprends les attaques.<br><span style="color:var(--cyan)">Apprends à défendre.</span></h2><p>Progresse avec des mini-cours, un terminal pédagogique, des défis guidés et des quiz. Teste uniquement les systèmes qui t'appartiennent ou pour lesquels tu as une autorisation.</p><button class="primary" onclick="showPage('learn')">Commencer le parcours →</button>
    <div class="stats"><div class="stat"><strong id="stat-xp">0 XP</strong><small>Points gagnés</small></div><div class="stat"><strong id="stat-done">0/6</strong><small>Modules terminés</small></div><div class="stat"><strong id="stat-badges">0</strong><small>Badges obtenus</small></div></div>
  </div>
  <div class="sectionhead"><div><h2>Reprendre l'entraînement</h2><p>Une étape à la fois : c'est comme ça qu'on progresse.</p></div></div>
  <div class="cards">
    <article class="panel"><div class="module"><div class="modicon">⌨</div><div><h3>Terminal Linux simulé</h3><p>Découvre <code>help</code>, <code>ls</code>, <code>pwd</code> et les permissions sans risque.</p></div></div><button onclick="showPage('terminal')">Ouvrir le terminal</button></article>
    <article class="panel"><div class="module"><div class="modicon">🛡</div><div><h3>Premier défi défense</h3><p>Repère les signaux d'un message de phishing et choisis une réponse sûre.</p></div></div><button onclick="showPage('challenges')">Lancer le défi</button></article>
  </div>
  <div class="sectionhead"><div><h2>Ta progression</h2><p>Les progrès sont enregistrés sur cet appareil.</p></div></div>
  <div class="panel"><div style="display:flex;justify-content:space-between;gap:12px"><strong>Parcours CyberLab</strong><span id="progress-label">0 %</span></div><div class="progress"><i id="overall-progress"></i></div><p class="hint">Astuce : lis le cours, puis termine son mini-défi pour valider un module.</p></div>
</section>
<section id="page-learn" class="page hidden">
  <div class="sectionhead"><div><h2>Parcours & cours</h2><p>Six modules courts avec un objectif concret pour chacun.</p></div></div>
  <div id="module-list" class="cards"></div>
  <div id="lesson-view" class="panel lesson hidden"></div>
</section>
<section id="page-terminal" class="page hidden">
  <div class="sectionhead"><div><h2>Terminal Linux pédagogique</h2><p>Un terminal simulé pour apprendre les commandes de base.</p></div><button class="ghost" onclick="resetTerminal()">Réinitialiser</button></div>
  <div class="callout"><strong>Important :</strong> ceci n'est pas un vrai shell. Il comprend uniquement une liste limitée de commandes d'apprentissage. Aucune commande système, scan réseau ou connexion externe n'est lancé.</div>
  <div class="terminal"><div class="termbar"><span><span class="dots"><i></i><i></i><i></i></span> &nbsp; cyberlab@lab:~</span><span>SIMULATEUR</span></div><div id="termout" class="termout" aria-live="polite"><span class="info">CyberLab Shell v1.0 — environnement fictif</span>
Tape <code>help</code> pour afficher les commandes disponibles.
Ce terminal est isolé et simulé.</div><form id="termform" class="termform"><span style="color:var(--cyan);padding-top:8px">›</span><input id="terminput" autocomplete="off" spellcheck="false" placeholder="Tape une commande, ex. help" aria-label="Commande simulée"><button class="primary">Exécuter</button></form></div>
  <p class="hint">Commandes disponibles : <code>help</code>, <code>pwd</code>, <code>ls</code>, <code>whoami</code>, <code>date</code>, <code>cat readme.txt</code>, <code>ip-info</code> (données fictives), <code>clear</code>, <code>quiz</code>.</p>
</section>
<section id="page-challenges" class="page hidden">
  <div class="sectionhead"><div><h2>Défis pratiques</h2><p>Des scénarios sûrs pour entraîner ton raisonnement.</p></div></div>
  <div class="panel"><div class="eyebrow">Défi 01 · Phishing</div><h2 style="margin:8px 0">Tu reçois ce message…</h2><div class="challenge" style="font-family:ui-monospace,monospace"><strong>De :</strong> support-securite@exemple-inconnu.test<br><strong>Objet :</strong> URGENT — ton compte sera fermé<br><br>« Clique ici immédiatement et saisis ton mot de passe pour éviter la suppression du compte. »</div><p>Que fais-tu en premier ?</p><div id="phish-choices"><button class="choice" onclick="answerChallenge('a')">A. Cliquer vite pour éviter la fermeture</button><button class="choice" onclick="answerChallenge('b')">B. Ne pas cliquer, vérifier via le site officiel ou un canal connu</button><button class="choice" onclick="answerChallenge('c')">C. Répondre avec mon mot de passe pour confirmer mon identité</button></div><div id="phish-feedback" aria-live="polite"></div></div>
  <div class="panel"><div class="eyebrow">Défi 02 · Mot de passe</div><h2 style="margin:8px 0">Renforcer un compte</h2><p>Tu utilises encore le même mot de passe sur plusieurs sites. Quelle amélioration est la plus solide ?</p><div id="pass-choices"><button class="choice" onclick="answerPassword('a')">A. Ajouter un point d'exclamation au même mot de passe</button><button class="choice" onclick="answerPassword('b')">B. Utiliser un mot de passe unique et long, stocké dans un gestionnaire, et activer le MFA</button><button class="choice" onclick="answerPassword('c')">C. Envoyer le mot de passe à un ami pour le garder en sécurité</button></div><div id="pass-feedback" aria-live="polite"></div></div>
  <div class="panel"><div class="eyebrow">Défi 03 · Permissions Linux</div><h2 style="margin:8px 0">Le principe du moindre privilège</h2><p>Un compte utilisateur doit-il avoir les droits administrateur en permanence ?</p><div id="perm-choices"><button class="choice" onclick="answerPerm('a')">A. Oui, c'est plus pratique</button><button class="choice" onclick="answerPerm('b')">B. Non, seulement lorsque c'est nécessaire et autorisé</button><button class="choice" onclick="answerPerm('c')">C. Oui, pour éviter de devoir mettre à jour le système</button></div><div id="perm-feedback" aria-live="polite"></div></div>
</section>
<section id="page-quiz" class="page hidden">
  <div class="sectionhead"><div><h2>Quiz de sécurité</h2><p>Teste tes connaissances. Chaque réponse affiche une explication.</p></div><button class="ghost" onclick="renderQuiz()">Recommencer</button></div>
  <div class="panel"><div id="quiz-content"></div><div id="quiz-result"></div></div>
</section>
<section id="page-badges" class="page hidden">
  <div class="sectionhead"><div><h2>Mes badges</h2><p>Débloque-les en terminant les leçons et les défis.</p></div></div><div id="badge-grid" class="badgegrid"></div>
  <div class="panel" style="margin-top:15px"><h3>Réinitialiser la progression</h3><p style="color:var(--muted)">Cette action efface les points, les modules terminés et les badges enregistrés dans ce navigateur.</p><button onclick="resetProgress()">Effacer ma progression</button></div>
</section>
<section id="page-glossary" class="page hidden">
  <div class="sectionhead"><div><h2>Glossaire essentiel</h2><p>Les mots que tu rencontreras en cybersécurité.</p></div></div><div class="glossary" id="glossary"></div>
</section>
<div class="footer">CyberLab Pro · Formation locale à but éducatif · Agis toujours avec autorisation.</div>
</main></div></div>
<script>
const modules=[
{id:'foundations',icon:'🧭',title:'Les bases de la cybersécurité',level:'Débutant',time:'8 min',desc:'Comprendre les menaces, les risques et la triade CIA.',sections:[
['Objectif','La cybersécurité protège les appareils, les comptes et les informations contre l’accès non autorisé, les altérations et les interruptions.'],
['La triade CIA','Confidentialité : seules les personnes autorisées voient les données. Intégrité : les données restent exactes. Disponibilité : les services restent accessibles.'],
['Risque et menace','Une menace est une source potentielle de dommage. Une vulnérabilité est une faiblesse. Le risque combine la probabilité et l’impact possible.'],
['À retenir','La sécurité est une suite d’habitudes et de contrôles, pas un seul logiciel magique. Les mises à jour, les sauvegardes et le MFA se complètent.']]},
{id:'network',icon:'🌐',title:'Réseaux et adresses IP',level:'Débutant',time:'10 min',desc:'Découvrir IP, DNS, routeur, HTTP et HTTPS.',sections:[
['Comment circule une donnée','Un réseau relie des appareils qui échangent des données selon des règles appelées protocoles. Un routeur dirige le trafic entre réseaux.'],
['Adresse IP et DNS','Une adresse IP identifie une interface sur un réseau. Le DNS traduit un nom de domaine en informations utiles pour trouver le service correspondant.'],
['HTTP et HTTPS','HTTPS protège la connexion avec TLS : il chiffre le trafic et aide à vérifier l’identité du serveur. Le cadenas ne garantit pas que le site est honnête.'],
['Pratique sûre','Sur ton propre réseau, apprends à reconnaître les appareils et à sécuriser le routeur. N’analyse pas le réseau d’autrui sans autorisation explicite.']]},
{id:'linux',icon:'⌨️',title:'Linux et terminal',level:'Débutant',time:'12 min',desc:'Naviguer dans des fichiers et comprendre les permissions.',sections:[
['Le shell','Un shell interprète des commandes. Dans ce logiciel, le terminal est une simulation sans accès à ton système réel.'],
['Commandes de base','pwd affiche le dossier courant ; ls liste les fichiers ; whoami affiche l’utilisateur ; cat lit un fichier texte.'],
['Permissions','Les permissions Linux distinguent lecture (r), écriture (w) et exécution (x), pour le propriétaire, le groupe et les autres.'],
['Bon réflexe','Comprends une commande avant de l’exécuter. Méfie-toi des commandes copiées depuis une source inconnue, surtout si elles utilisent des privilèges élevés.']]},
{id:'passwords',icon:'🔐',title:'Mots de passe et MFA',level:'Débutant',time:'8 min',desc:'Protéger ses comptes avec des identifiants robustes.',sections:[
['Mots de passe uniques','Un mot de passe long et unique réduit le risque qu’une fuite sur un site compromette aussi tes autres comptes. Un gestionnaire de mots de passe aide à les créer et les conserver.'],
['Qu’est-ce que le MFA ?','L’authentification multifacteur demande au moins deux types de preuves : ce que tu connais, ce que tu possèdes ou ce que tu es.'],
['Méthodes plus solides','Une clé de sécurité ou une passkey résiste généralement mieux au phishing que les codes SMS. Une application d’authentification est souvent préférable au SMS.'],
['Si un compte est compromis','Change le mot de passe depuis le site officiel, ferme les sessions inconnues, vérifie les méthodes de récupération et active le MFA.']]},
{id:'phishing',icon:'🎣',title:'Reconnaître le phishing',level:'Débutant',time:'9 min',desc:'Repérer l’urgence, les liens suspects et les demandes secrètes.',sections:[
['Signaux d’alerte','Urgence inhabituelle, menace de fermeture, adresse d’expéditeur étrange, lien inattendu ou demande de mot de passe/code sont des signaux d’alerte.'],
['Vérifier sans cliquer','Ouvre le site en saisissant toi-même son adresse ou utilise l’application officielle. Contacte l’organisation via un numéro ou canal connu.'],
['Si tu as cliqué','Ne panique pas. Ne fournis rien de plus, signale le message, lance les mesures de sécurité appropriées et change tout identifiant transmis depuis le site officiel.'],
['Règle d’or','Un service légitime ne devrait pas te demander de lui envoyer ton mot de passe. Ne partage jamais un code MFA de connexion.']]},
{id:'defense',icon:'🛡️',title:'Défense et réponse aux incidents',level:'Débutant +',time:'11 min',desc:'Sauvegardes, mises à jour, moindre privilège et réaction.',sections:[
['Réduire la surface d’attaque','Désinstalle les applications inutiles, mets à jour tes appareils, verrouille les comptes et limite les permissions.'],
['Sauvegardes','Garde des copies de tes fichiers importants, dont au moins une copie séparée de l’appareil principal. Vérifie périodiquement que tu peux restaurer les fichiers.'],
['Moindre privilège','Un compte ne doit disposer que des droits nécessaires à sa tâche. Les privilèges administrateur ne s’utilisent que lorsque c’est nécessaire.'],
['Réagir à un incident','Isole l’appareil compromis si besoin, préserve les informations utiles, signale l’incident et change les identifiants depuis un appareil sûr. Pour un incident professionnel, suis la procédure de ton organisation.']]}
];
const glossaryItems=[
['MFA','Authentification multifacteur : au moins deux preuves différentes pour vérifier une connexion.'],
['Phishing','Tentative de tromper une personne pour lui faire révéler des informations ou réaliser une action.'],
['Pare-feu','Contrôle les connexions réseau selon des règles définies.'],
['DNS','Service qui aide à associer un nom de domaine à des informations réseau.'],
['Adresse IP','Identifiant réseau utilisé pour acheminer les données vers une interface.'],
['Chiffrement','Transformation de données pour les rendre illisibles sans la clé appropriée.'],
['Vulnérabilité','Faiblesse qui peut être exploitée et provoquer un impact.'],
['Correctif','Mise à jour qui corrige notamment des défauts ou failles.'],
['Hachage','Transformation à sens unique utilisée, entre autres, pour vérifier des données. Les mots de passe doivent être hachés avec une fonction adaptée.'],
['MFA résistant au phishing','Méthode comme une passkey ou une clé de sécurité qui lie l’authentification au service attendu.'],
['Moindre privilège','Principe qui accorde uniquement les droits indispensables.'],
['Journalisation','Enregistrement d’événements utiles à la détection et à l’analyse.']
];
const quizItems=[
{q:'Que signifie le « C » de la triade CIA en sécurité ?',opts:['Connexion','Confidentialité','Correction'],a:1,why:'La confidentialité limite l’accès aux données aux personnes autorisées.'},
{q:'Tu reçois un lien menaçant de fermer ton compte dans 10 minutes. Quel est le meilleur réflexe ?',opts:['Cliquer immédiatement','Répondre avec ton mot de passe','Vérifier via le site ou l’application officielle'],a:2,why:'L’urgence est une tactique courante. Vérifie par un canal connu, sans utiliser le lien reçu.'},
{q:'À quoi sert le MFA ?',opts:['Ajouter une ou plusieurs preuves à la connexion','Remplacer toutes les mises à jour','Rendre les mots de passe publics'],a:0,why:'Le MFA ajoute des preuves différentes et réduit la dépendance au seul mot de passe.'},
{q:'Pourquoi ne faut-il pas réutiliser le même mot de passe ?',opts:['Parce que les mots de passe ne fonctionnent qu’une fois','Une fuite sur un site pourrait compromettre d’autres comptes','Cela ralentit toujours Internet'],a:1,why:'Des mots de passe uniques limitent les dégâts lorsqu’un service subit une fuite.'},
{q:'Que signifie le principe du moindre privilège ?',opts:['Tout le monde doit être administrateur','Accorder seulement les droits nécessaires','Désactiver les sauvegardes'],a:1,why:'Limiter les droits réduit les dommages possibles en cas d’erreur ou de compromission.'},
{q:'HTTPS garantit-il qu’un site est honnête ?',opts:['Oui, toujours','Non : il protège la connexion mais le site peut être malveillant','Seulement sur téléphone'],a:1,why:'HTTPS protège le transport et l’identité du serveur, pas la fiabilité de tout contenu du site.'}
];
const badgeDefs=[['firstlesson','📘','Premier cours','Termine un module.'],['phishingpro','🎣','Œil anti-phishing','Réussis le défi phishing.'],['passwordguardian','🔐','Gardien des comptes','Réussis le défi mots de passe.'],['terminalstarter','⌨️','Terminal en main','Utilise une commande simulée.'],['quizstarter','🧠','Esprit sécurité','Réussis au moins 5 questions du quiz.'],['pathfinder','🏆','Parcours terminé','Termine les six modules.']];
let state={xp:0,done:[],badges:[],terminalUsed:false,quizBest:0};
try{const saved=JSON.parse(localStorage.getItem('cyberlabpro_state')||'null');if(saved)state={...state,...saved}}catch(e){}
function save(){try{localStorage.setItem('cyberlabpro_state',JSON.stringify(state))}catch(e){}updateStats();renderBadges()}
function award(id,xp=0){let added=false;if(id&&!state.badges.includes(id)){state.badges.push(id);added=true}if(xp){state.xp+=xp;added=true}if(added)save()}
function updateStats(){document.getElementById('stat-xp').textContent=state.xp+' XP';document.getElementById('stat-done').textContent=state.done.length+'/6';document.getElementById('stat-badges').textContent=state.badges.length;let p=Math.round(state.done.length/6*100);document.getElementById('overall-progress').style.width=p+'%';document.getElementById('progress-label').textContent=p+'%'}
function showPage(page){document.querySelectorAll('.page').forEach(x=>x.classList.add('hidden'));document.getElementById('page-'+page).classList.remove('hidden');document.querySelectorAll('.navbtn').forEach(x=>x.classList.toggle('active',x.dataset.page===page));if(page==='learn')renderModules();if(page==='badges')renderBadges();if(page==='glossary')renderGlossary();window.scrollTo({top:0,behavior:'smooth'})}
document.querySelectorAll('.navbtn').forEach(b=>b.addEventListener('click',()=>showPage(b.dataset.page)));
function renderModules(){document.getElementById('module-list').innerHTML=modules.map((m,i)=>`<article class="panel"><div class="module"><div class="modicon">${m.icon}</div><div><h3>${m.title}</h3><p>${m.desc}</p></div></div><div class="meta"><span>${m.level}</span><span>${m.time}</span><span>${state.done.includes(m.id)?'✓ Terminé':'À apprendre'}</span></div><div class="progress"><i style="width:${state.done.includes(m.id)?'100':'0'}%"></i></div><button onclick="openLesson('${m.id}')">${state.done.includes(m.id)?'Revoir le cours':'Étudier le module'} →</button></article>`).join('')}
function openLesson(id){let m=modules.find(x=>x.id===id);let v=document.getElementById('lesson-view');v.classList.remove('hidden');v.innerHTML=`<div class="eyebrow">Module · ${m.level} · ${m.time}</div><h2>${m.icon} ${m.title}</h2><p style="color:var(--muted)">${m.desc}</p>${m.sections.map((s,i)=>`<h3>${i+1}. ${s[0]}</h3><p>${s[1]}</p>`).join('')}<div class="callout"><strong>À toi :</strong> après lecture, valide ce module. Essaie ensuite les défis et le quiz pour consolider tes connaissances.</div><button class="primary" onclick="completeModule('${m.id}')">${state.done.includes(m.id)?'Module déjà validé ✓':'Marquer le module terminé +50 XP'}</button> <button onclick="document.getElementById('lesson-view').classList.add('hidden')">Fermer le cours</button>`;v.scrollIntoView({behavior:'smooth',block:'start'})}
function completeModule(id){if(!state.done.includes(id)){state.done.push(id);state.xp+=50;award('firstlesson');if(state.done.length===6)award('pathfinder',100);save();renderModules();openLesson(id)}}
function appendTerminal(text,cls=''){let out=document.getElementById('termout');let line=document.createElement('div');line.className=cls;line.textContent=text;out.appendChild(line);out.scrollTop=out.scrollHeight}
function resetTerminal(){document.getElementById('termout').textContent='CyberLab Shell v1.0 — environnement fictif\nTape help pour afficher les commandes disponibles.\nCe terminal est isolé et simulé.';document.getElementById('terminput').value=''}
document.getElementById('termform').addEventListener('submit',e=>{e.preventDefault();let input=document.getElementById('terminput'),cmd=input.value.trim();if(!cmd)return;appendTerminal('cyberlab@lab:~$ '+cmd,'info');input.value='';let responses={
help:['Commandes simulées : help, pwd, ls, whoami, date, cat readme.txt, ip-info, quiz, clear.','Astuce : ces commandes sont pédagogiques et n’accèdent pas à ton vrai appareil.'],
pwd:['/home/apprenant'],
ls:['readme.txt  cours/  exercices/  notes.txt'],
whoami:['apprenant (utilisateur fictif, sans privilèges administrateur)'],
date:['2026-10-29 (date d’exemple du laboratoire)'],
'cat readme.txt':['Bienvenue dans CyberLab !','Règle : pratique uniquement sur des systèmes que tu possèdes ou pour lesquels tu as une autorisation.'],
'ip-info':['Interface fictive : eth0','Adresse privée d’exemple : 192.168.1.25/24','Passerelle d’exemple : 192.168.1.1','Aucune information réseau réelle n’a été consultée.'],
quiz:['Question : quelle commande affiche le dossier courant ?','Réponse : pwd. Essaie ensuite la commande pwd dans le terminal.'],
clear:[]
};
if(cmd==='clear'){document.getElementById('termout').textContent='';}
else if(responses[cmd])responses[cmd].forEach(t=>appendTerminal(t,cmd==='ip-info'?'warn':''));
else if(/^(sudo|rm|nmap|ping|curl|wget|ssh|nc|netcat|python|bash|sh|chmod|chown|apt|systemctl)\b/i.test(cmd)){appendTerminal('Commande non exécutée : ce simulateur n’autorise pas cette commande.','bad');appendTerminal('Pour apprendre en sécurité, utilise uniquement les exercices guidés intégrés.','warn')}
else appendTerminal('Commande inconnue. Tape help pour voir la liste autorisée.','warn');
if(!state.terminalUsed){state.terminalUsed=true;award('terminalstarter',10)}});
function markChoice(containerId,btn,correct){document.querySelectorAll('#'+containerId+' .choice').forEach(b=>b.disabled=true);btn.classList.add(correct?'correct':'wrong')}
function answerChallenge(choice){let btn=[...document.querySelectorAll('#phish-choices button')].find(b=>b.textContent.startsWith(choice.toUpperCase()+'.'));let ok=choice==='b';markChoice('phish-choices',btn,ok);document.getElementById('phish-feedback').innerHTML=ok?'<div class="toast">Exact ! +30 XP. Ne clique pas : vérifie l’expéditeur et utilise un canal officiel connu.</div>':'<div class="callout warning">Pas tout à fait. L’urgence et la demande de mot de passe sont des signaux d’alerte. Choisis B : vérifie par un canal officiel.</div>';if(ok&&!state.badges.includes('phishingpro'))award('phishingpro',30)}
function answerPassword(choice){let btn=[...document.querySelectorAll('#pass-choices button')].find(b=>b.textContent.startsWith(choice.toUpperCase()+'.'));let ok=choice==='b';markChoice('pass-choices',btn,ok);document.getElementById('pass-feedback').innerHTML=ok?'<div class="toast">Bien joué ! +30 XP. Un mot de passe unique et long, un gestionnaire et le MFA se complètent.</div>':'<div class="callout warning">Essaie encore : la meilleure option est B. Un mot de passe unique limite les dégâts d’une fuite et le MFA ajoute une protection.</div>';if(ok&&!state.badges.includes('passwordguardian'))award('passwordguardian',30)}
function answerPerm(choice){let btn=[...document.querySelectorAll('#perm-choices button')].find(b=>b.textContent.startsWith(choice.toUpperCase()+'.'));let ok=choice==='b';markChoice('perm-choices',btn,ok);document.getElementById('perm-feedback').innerHTML=ok?'<div class="toast">Exact ! +30 XP. Moins de privilèges signifie moins de dégâts possibles.</div>':'<div class="callout warning">La bonne réponse est B : n’accorde que les droits nécessaires, et seulement quand il le faut.</div>';if(ok)award(null,30)}
let quizAnswers={};
function renderQuiz(){quizAnswers={};document.getElementById('quiz-result').innerHTML='';document.getElementById('quiz-content').innerHTML=quizItems.map((q,i)=>`<div class="quizq" id="qq${i}"><p>${i+1}. ${q.q}</p>${q.opts.map((o,j)=>`<button class="choice" onclick="selectQuiz(${i},${j},this)">${String.fromCharCode(65+j)}. ${o}</button>`).join('')}<div class="hint" id="qwhy${i}"></div></div>`).join('')+'<button class="primary" onclick="submitQuiz()">Calculer mon score</button>'}
function selectQuiz(i,j,btn){if(quizAnswers[i]!==undefined)return;quizAnswers[i]=j;let q=quizItems[i];document.querySelectorAll('#qq'+i+' button').forEach((b,k)=>{b.disabled=true;if(k===q.a)b.classList.add('correct')});if(j!==q.a)btn.classList.add('wrong');document.getElementById('qwhy'+i).textContent=(j===q.a?'Bonne réponse. ':'Explication : ')+q.why}
function submitQuiz(){let answered=Object.keys(quizAnswers).length;if(answered<quizItems.length){document.getElementById('quiz-result').innerHTML='<div class="callout warning">Réponds aux six questions avant de calculer ton score.</div>';return}let score=quizItems.filter((q,i)=>quizAnswers[i]===q.a).length;document.getElementById('quiz-result').innerHTML=`<div class="toast">Ton score : ${score}/${quizItems.length}. ${score>=5?'Excellent travail !':score>=3?'Bon début : relis les explications pour progresser.':'Continue à apprendre puis réessaie.'}</div>`;if(score>state.quizBest)state.quizBest=score;if(score>=5)award('quizstarter',50);save()}
function renderBadges(){let el=document.getElementById('badge-grid');if(!el)return;el.innerHTML=badgeDefs.map(b=>{let unlocked=state.badges.includes(b[0]);return `<div class="badgecard ${unlocked?'':'locked'}"><div class="big">${b[1]}</div><strong>${b[2]}</strong><small>${unlocked?'Débloqué ✓':b[3]}</small></div>`}).join('')}
function renderGlossary(){document.getElementById('glossary').innerHTML=glossaryItems.map(x=>`<div class="term"><strong>${x[0]}</strong><p>${x[1]}</p></div>`).join('')}
function resetProgress(){if(confirm('Effacer toute la progression CyberLab sur cet appareil ?')){state={xp:0,done:[],badges:[],terminalUsed:false,quizBest:0};save();renderModules();renderBadges();alert('Progression effacée.')}}
renderModules();renderQuiz();renderBadges();renderGlossary();updateStats();
</script>
</body></html>'''
path = Path("/mnt/data/CyberLab_Pro_Cybersecurite.html")
path.write_text(html, encoding="utf-8")
print(f"Fichier créé : {path} ({path.stat().st_size:,} octets)")
