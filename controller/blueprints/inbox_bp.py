#Purpose render tempaltes related to viewing workshop content
from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from model import workshop
from model import enroll
from jinja2.exceptions import TemplateNotFound

