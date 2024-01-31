#!/usr/bin/python
#coding utf-8
import sqlite3

connection =sqlite3.connect("a.db")
connection.execute("create table students (name text,age int)")
connection.execute("insert into students values ('zhangsan','14')")
connection.execute("insert into students values ('lisi','18')")
connection.execute("insert into students values ('mhb','20')")
connection.execute("commit")