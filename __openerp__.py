# -*- coding: utf-8 -*-

{
  "name" : "InfoSaône - Module OpenERP Tutoriel 05",
  "version" : "0.1",
  "author" : "InfoSaône",
  "category" : "InfoSaône/Tutoriel",


  'description': """
InfoSaône / Module OpenERP Tutoriel 05 
===================================================

Le but de ce module est de montrer comment modifier une vue (liste) existante

Ce module installe le module CRM pour pouvoir modifier la vue liste des clients `base.view_partner_tree`

Le fichier `infosaone_partner_view.xml` contient les modifications éffectuées.

""",

  'maintainer': 'InfoSaône',
  'website': 'http://www.infosaone.com',
  "depends" : ["base","crm"],  # Liste des dépendances (autres modules nececessaire au fonctionnement de celui-ci)
  "init_xml" : [],             # Liste des fichiers XML à installer uniquement lors de l'installation du module
  "demo_xml" : [],             # Liste des fichiers XML à installer pour charger les données de démonstration

  "update_xml" : ["infosaone_partner_view.xml"], # Liste des fichiers XML à installer lors d'une mise à jour du module (ou lord de l'installation)

  "installable": True,         # Si False, ce module sera visible mais non installable (intéret ?)
  "active": False              # Si True, ce module sera installé automatiquement dés la création de la base de données d'OpenERP
}





