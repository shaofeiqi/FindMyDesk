from flask import Flask, request, render_template, redirect, url_for, jsonify, session
from flask_sqlalchemy import SQLAlchemy
from librarydb.library import db, Library, Floor, Seat

app = Flask(__name__)
app.secret_key = 'FindDesk'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///findmydesk.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)


# Adding more seats to the dataset
def insert_seats():
  Bulter = Library(
      name='Butler',
      floors=[
          Floor(number='1',
                map_image_url='images/Butler_Floors/Butler_2nd.png',
                seats=[
                    Seat(label='A1',
                         top_position=31,
                         left_position=24,
                         available=True),
                    Seat(label='A2',
                         top_position=35,
                         left_position=24,
                         available=True),
                    Seat(label='A3',
                         top_position=39,
                         left_position=24,
                         available=True),
                    Seat(label='A4',
                         top_position=43,
                         left_position=24,
                         available=True),
                    Seat(label='A5',
                         top_position=48,
                         left_position=24,
                         available=True),
                    Seat(label='A6',
                         top_position=52,
                         left_position=24,
                         available=True),
                    Seat(label='A7',
                         top_position=56,
                         left_position=24,
                         available=True),
                    Seat(label='A8',
                         top_position=60,
                         left_position=24,
                         available=True),
                    Seat(label='A9',
                         top_position=31,
                         left_position=26.5,
                         available=True),
                    Seat(label='A10',
                         top_position=35,
                         left_position=26.5,
                         available=True),
                    Seat(label='A11',
                         top_position=39,
                         left_position=26.5,
                         available=True),
                    Seat(label='A12',
                         top_position=43,
                         left_position=26.5,
                         available=True),
                    Seat(label='A13',
                         top_position=48,
                         left_position=26.5,
                         available=True),
                    Seat(label='A14',
                         top_position=52,
                         left_position=26.5,
                         available=True),
                    Seat(label='A15',
                         top_position=56,
                         left_position=26.5,
                         available=True),
                    Seat(label='A16',
                         top_position=60,
                         left_position=26.5,
                         available=True),
                    Seat(label='A17',
                         top_position=31,
                         left_position=29,
                         available=True),
                    Seat(label='A18',
                         top_position=35,
                         left_position=29,
                         available=True),
                    Seat(label='A19',
                         top_position=39,
                         left_position=29,
                         available=True),
                    Seat(label='A20',
                         top_position=43,
                         left_position=29,
                         available=True),
                    Seat(label='A21',
                         top_position=48,
                         left_position=29,
                         available=True),
                    Seat(label='A22',
                         top_position=52,
                         left_position=29,
                         available=True),
                    Seat(label='A23',
                         top_position=56,
                         left_position=29,
                         available=True),
                    Seat(label='A24',
                         top_position=60,
                         left_position=29,
                         available=True),
                    Seat(label='A25',
                         top_position=31,
                         left_position=31.5,
                         available=True),
                    Seat(label='A26',
                         top_position=35,
                         left_position=31.5,
                         available=True),
                    Seat(label='A27',
                         top_position=39,
                         left_position=31.5,
                         available=True),
                    Seat(label='A28',
                         top_position=43,
                         left_position=31.5,
                         available=True),
                    Seat(label='A29',
                         top_position=48,
                         left_position=31.5,
                         available=True),
                    Seat(label='A30',
                         top_position=52,
                         left_position=31.5,
                         available=True),
                    Seat(label='A31',
                         top_position=56,
                         left_position=31.5,
                         available=True),
                    Seat(label='A32',
                         top_position=60,
                         left_position=31.5,
                         available=True)
                ]),
          Floor(number='2',
                map_image_url='images/Butler_Floors/Butler_2nd.png',
                seats=[
                    Seat(label='A1',
                         top_position=31,
                         left_position=24,
                         available=True),
                    Seat(label='A2',
                         top_position=35,
                         left_position=24,
                         available=True),
                    Seat(label='A3',
                         top_position=39,
                         left_position=24,
                         available=True),
                    Seat(label='A4',
                         top_position=43,
                         left_position=24,
                         available=True),
                    Seat(label='A5',
                         top_position=48,
                         left_position=24,
                         available=True),
                    Seat(label='A6',
                         top_position=52,
                         left_position=24,
                         available=True),
                    Seat(label='A7',
                         top_position=56,
                         left_position=24,
                         available=True),
                    Seat(label='A8',
                         top_position=60,
                         left_position=24,
                         available=True),
                    Seat(label='A9',
                         top_position=31,
                         left_position=26.5,
                         available=True),
                    Seat(label='A10',
                         top_position=35,
                         left_position=26.5,
                         available=True),
                    Seat(label='A11',
                         top_position=39,
                         left_position=26.5,
                         available=True),
                    Seat(label='A12',
                         top_position=43,
                         left_position=26.5,
                         available=True),
                    Seat(label='A13',
                         top_position=48,
                         left_position=26.5,
                         available=True),
                    Seat(label='A14',
                         top_position=52,
                         left_position=26.5,
                         available=True),
                    Seat(label='A15',
                         top_position=56,
                         left_position=26.5,
                         available=True),
                    Seat(label='A16',
                         top_position=60,
                         left_position=26.5,
                         available=True),
                    Seat(label='A17',
                         top_position=31,
                         left_position=29,
                         available=True),
                    Seat(label='A18',
                         top_position=35,
                         left_position=29,
                         available=True),
                    Seat(label='A19',
                         top_position=39,
                         left_position=29,
                         available=True),
                    Seat(label='A20',
                         top_position=43,
                         left_position=29,
                         available=True),
                    Seat(label='A21',
                         top_position=48,
                         left_position=29,
                         available=True),
                    Seat(label='A22',
                         top_position=52,
                         left_position=29,
                         available=True),
                    Seat(label='A23',
                         top_position=56,
                         left_position=29,
                         available=True),
                    Seat(label='A24',
                         top_position=60,
                         left_position=29,
                         available=True),
                    Seat(label='A25',
                         top_position=31,
                         left_position=31.5,
                         available=True),
                    Seat(label='A26',
                         top_position=35,
                         left_position=31.5,
                         available=True),
                    Seat(label='A27',
                         top_position=39,
                         left_position=31.5,
                         available=True),
                    Seat(label='A28',
                         top_position=43,
                         left_position=31.5,
                         available=True),
                    Seat(label='A29',
                         top_position=48,
                         left_position=31.5,
                         available=True),
                    Seat(label='A30',
                         top_position=52,
                         left_position=31.5,
                         available=True),
                    Seat(label='A31',
                         top_position=56,
                         left_position=31.5,
                         available=True),
                    Seat(label='A32',
                         top_position=60,
                         left_position=31.5,
                         available=True)
                ]),
          Floor(number='3',
                map_image_url='images/Butler_Floors/Butler_3rd.png',
                seats=[
                    Seat(label='C1',
                         top_position=31,
                         left_position=66,
                         available=True),
                    Seat(label='C2',
                         top_position=35,
                         left_position=66,
                         available=True),
                    Seat(label='C3',
                         top_position=39,
                         left_position=66,
                         available=True),
                    Seat(label='C4',
                         top_position=43,
                         left_position=66,
                         available=True),
                    Seat(label='C5',
                         top_position=31,
                         left_position=68.5,
                         available=True),
                    Seat(label='C6',
                         top_position=35,
                         left_position=68.5,
                         available=True),
                    Seat(label='C7',
                         top_position=39,
                         left_position=68.5,
                         available=True),
                    Seat(label='C8',
                         top_position=43,
                         left_position=68.5,
                         available=True),
                    Seat(label='C9',
                         top_position=31,
                         left_position=71,
                         available=True),
                    Seat(label='C10',
                         top_position=35,
                         left_position=71,
                         available=True),
                    Seat(label='C11',
                         top_position=39,
                         left_position=71,
                         available=True),
                    Seat(label='C12',
                         top_position=43,
                         left_position=71,
                         available=True),
                    Seat(label='C13',
                         top_position=31,
                         left_position=73.5,
                         available=True),
                    Seat(label='C14',
                         top_position=35,
                         left_position=73.5,
                         available=True),
                    Seat(label='C15',
                         top_position=39,
                         left_position=73.5,
                         available=True),
                    Seat(label='C16',
                         top_position=43,
                         left_position=73.5,
                         available=True),
                ]),
          Floor(number='4',
                map_image_url='images/Butler_Floors/Butler_4th.png',
                seats=[
                    Seat(label='D1',
                         top_position=31,
                         left_position=24,
                         available=True),
                    Seat(label='D2',
                         top_position=35,
                         left_position=24,
                         available=True),
                    Seat(label='D3',
                         top_position=39,
                         left_position=24,
                         available=True),
                    Seat(label='D4',
                         top_position=43,
                         left_position=24,
                         available=True),
                    Seat(label='D5',
                         top_position=48,
                         left_position=24,
                         available=True),
                    Seat(label='D6',
                         top_position=52,
                         left_position=24,
                         available=True),
                    Seat(label='D7',
                         top_position=56,
                         left_position=24,
                         available=True),
                    Seat(label='D8',
                         top_position=60,
                         left_position=24,
                         available=True),
                    Seat(label='D9',
                         top_position=31,
                         left_position=26.5,
                         available=True),
                    Seat(label='D10',
                         top_position=35,
                         left_position=26.5,
                         available=True),
                    Seat(label='D11',
                         top_position=39,
                         left_position=26.5,
                         available=True),
                    Seat(label='D12',
                         top_position=43,
                         left_position=26.5,
                         available=True),
                    Seat(label='D13',
                         top_position=48,
                         left_position=26.5,
                         available=True),
                    Seat(label='D14',
                         top_position=52,
                         left_position=26.5,
                         available=True),
                    Seat(label='D15',
                         top_position=56,
                         left_position=26.5,
                         available=True),
                    Seat(label='D16',
                         top_position=60,
                         left_position=26.5,
                         available=True),
                    Seat(label='D17',
                         top_position=31,
                         left_position=29.0,
                         available=True),
                    Seat(label='D18',
                         top_position=35,
                         left_position=29.0,
                         available=True),
                    Seat(label='D19',
                         top_position=39,
                         left_position=29.0,
                         available=True),
                    Seat(label='D20',
                         top_position=43,
                         left_position=29.0,
                         available=True),
                    Seat(label='D21',
                         top_position=48,
                         left_position=29.0,
                         available=True),
                    Seat(label='D22',
                         top_position=52,
                         left_position=29.0,
                         available=True),
                    Seat(label='D23',
                         top_position=56,
                         left_position=29.0,
                         available=True),
                    Seat(label='D24',
                         top_position=60,
                         left_position=29.0,
                         available=True),
                    Seat(label='D25',
                         top_position=31,
                         left_position=31.5,
                         available=True),
                    Seat(label='D26',
                         top_position=35,
                         left_position=31.5,
                         available=True),
                    Seat(label='D27',
                         top_position=39,
                         left_position=31.5,
                         available=True),
                    Seat(label='D28',
                         top_position=43,
                         left_position=31.5,
                         available=True),
                    Seat(label='D29',
                         top_position=48,
                         left_position=31.5,
                         available=True),
                    Seat(label='D30',
                         top_position=52,
                         left_position=31.5,
                         available=True),
                    Seat(label='D31',
                         top_position=56,
                         left_position=31.5,
                         available=True),
                    Seat(label='D32',
                         top_position=60,
                         left_position=31.5,
                         available=True)
                ]),
          Floor(number='5',
                map_image_url='images/Butler_Floors/Butler_5th.png',
                seats=[
                    Seat(label='E1',
                         top_position=10,
                         left_position=10,
                         available=True),
                    Seat(label='E2',
                         top_position=20,
                         left_position=20,
                         available=True),
                    Seat(label='E3',
                         top_position=30,
                         left_position=30,
                         available=True),
                    Seat(label='E4',
                         top_position=40,
                         left_position=40,
                         available=True)
                ]),
          Floor(number='6',
                map_image_url='images/Butler_Floors/Butler_6th.png',
                seats=[
                    Seat(label='F1',
                         top_position=10,
                         left_position=10,
                         available=True),
                    Seat(label='F2', top_position=20, available=True),
                    Seat(label='F3',
                         top_position=30,
                         left_position=30,
                         available=True),
                    Seat(label='F4',
                         top_position=40,
                         left_position=40,
                         available=True)
                ]),
      ])
  db.session.add(Bulter)

  Milstein = Library(
      name='Milstein',
      floors=[
          Floor(number='1',
                map_image_url='images/Milstein_Floors/MLC_1st.png',
                seats=[
                    Seat(label='A1',
                         top_position=33.5,
                         left_position=35.2,
                         available=True),
                    Seat(label='A2',
                         top_position=33.5,
                         left_position=52.8,
                         available=True),
                    Seat(label='A3',
                         top_position=43.2,
                         left_position=17.6,
                         available=True),
                    Seat(label='A4',
                         top_position=43.2,
                         left_position=20.4,
                         available=True),
                    Seat(label='A5',
                         top_position=47.2,
                         left_position=17.6,
                         available=True),
                    Seat(label='A6',
                         top_position=47.2,
                         left_position=20.4,
                         available=True),
                    Seat(label='A7',
                         top_position=56,
                         left_position=28.5,
                         available=True),
                    Seat(label='A8',
                         top_position=60,
                         left_position=28.5,
                         available=True),
                    Seat(label='A9',
                         top_position=64,
                         left_position=28.5,
                         available=True),
                    Seat(label='A10',
                         top_position=56,
                         left_position=32.8,
                         available=True),
                    Seat(label='A11',
                         top_position=60,
                         left_position=32.8,
                         available=True),
                    Seat(label='A12',
                         top_position=64,
                         left_position=32.8,
                         available=True),
                    Seat(label='A13',
                         top_position=56,
                         left_position=35.6,
                         available=True),
                    Seat(label='A14',
                         top_position=60,
                         left_position=35.6,
                         available=True),
                    Seat(label='A15',
                         top_position=64,
                         left_position=35.6,
                         available=True),
                    Seat(label='A16',
                         top_position=56,
                         left_position=38.4,
                         available=True),
                    Seat(label='A17',
                         top_position=60,
                         left_position=38.4,
                         available=True),
                    Seat(label='A18',
                         top_position=64,
                         left_position=38.4,
                         available=True),
                    Seat(label='A19',
                         top_position=60.5,
                         left_position=52.2,
                         available=True),
                    Seat(label='A20',
                         top_position=56,
                         left_position=61,
                         available=True),
                    Seat(label='A21',
                         top_position=60,
                         left_position=61,
                         available=True),
                    Seat(label='A22',
                         top_position=64,
                         left_position=61,
                         available=True),
                    Seat(label='A23',
                         top_position=38,
                         left_position=60,
                         available=True),
                    Seat(label='A24',
                         top_position=42,
                         left_position=60,
                         available=True),
                    Seat(label='A25',
                         top_position=46,
                         left_position=60,
                         available=True),
                    Seat(label='A26',
                         top_position=42,
                         left_position=64,
                         available=True),
                    Seat(label='A27',
                         top_position=47,
                         left_position=64,
                         available=True),
                ]),
          Floor(number='2',
                map_image_url='images/Milstein_Floors/MLC_2nd.png',
                seats=[
                    Seat(label='B1',
                         top_position=20,
                         left_position=10,
                         available=True),
                    Seat(label='B2',
                         top_position=24,
                         left_position=10,
                         available=True),
                    Seat(label='B3',
                         top_position=28,
                         left_position=10,
                         available=True),
                    Seat(label='B4',
                         top_position=42,
                         left_position=9.5,
                         available=True),
                    Seat(label='B5',
                         top_position=38,
                         left_position=21,
                         available=True),
                    Seat(label='B6',
                         top_position=42,
                         left_position=21,
                         available=True),
                    Seat(label='B7',
                         top_position=46,
                         left_position=21,
                         available=True),
                    Seat(label='B8',
                         top_position=38,
                         left_position=26,
                         available=True),
                    Seat(label='B9',
                         top_position=42,
                         left_position=26,
                         available=True),
                    Seat(label='B10',
                         top_position=46,
                         left_position=26,
                         available=True),
                    Seat(label='B11',
                         top_position=54,
                         left_position=25,
                         available=True),
                    Seat(label='B12',
                         top_position=54,
                         left_position=29,
                         available=True),
                    Seat(label='B13',
                         top_position=54,
                         left_position=33,
                         available=True),
                    Seat(label='B14',
                         top_position=54,
                         left_position=46,
                         available=True),
                    Seat(label='B15',
                         top_position=54,
                         left_position=50,
                         available=True),
                    Seat(label='B16',
                         top_position=21,
                         left_position=43,
                         available=True),
                    Seat(label='B17',
                         top_position=27,
                         left_position=43,
                         available=True),
                    Seat(label='B18',
                         top_position=64,
                         left_position=69,
                         available=True),
                    Seat(label='B19',
                         top_position=64,
                         left_position=74,
                         available=True),
                    Seat(label='B20',
                         top_position=53,
                         left_position=58.5,
                         available=True),
                    Seat(label='B21',
                         top_position=27,
                         left_position=70.2,
                         available=True)
                ]),
          Floor(number='3',
                map_image_url='images/Milstein_Floors/MLC_3rd.png',
                seats=[
                    Seat(label='C1',
                         top_position=21,
                         left_position=23,
                         available=True),
                    Seat(label='C2',
                         top_position=25,
                         left_position=23,
                         available=True),
                    Seat(label='C3',
                         top_position=29,
                         left_position=23,
                         available=True),
                    Seat(label='C4',
                         top_position=21,
                         left_position=26,
                         available=True),
                    Seat(label='C5',
                         top_position=25,
                         left_position=26,
                         available=True),
                    Seat(label='C6',
                         top_position=29,
                         left_position=26,
                         available=True),
                    Seat(label='C7',
                         top_position=39,
                         left_position=22,
                         available=True),
                    Seat(label='C8',
                         top_position=39,
                         left_position=24,
                         available=True),
                    Seat(label='C9',
                         top_position=44,
                         left_position=22,
                         available=True),
                    Seat(label='C10',
                         top_position=44,
                         left_position=24,
                         available=True),
                    Seat(label='C11',
                         top_position=21,
                         left_position=42,
                         available=True),
                    Seat(label='C12',
                         top_position=25,
                         left_position=42,
                         available=True),
                    Seat(label='C13',
                         top_position=29,
                         left_position=42,
                         available=True),
                    Seat(label='C14',
                         top_position=21,
                         left_position=63,
                         available=True),
                    Seat(label='C15',
                         top_position=25,
                         left_position=63,
                         available=True),
                    Seat(label='C16',
                         top_position=29,
                         left_position=63,
                         available=True),
                    Seat(label='C17',
                         top_position=55,
                         left_position=70,
                         available=True),
                    Seat(label='C18',
                         top_position=60,
                         left_position=70,
                         available=True),
                    Seat(label='C19',
                         top_position=64,
                         left_position=70,
                         available=True),
                    Seat(label='C20',
                         top_position=55,
                         left_position=76,
                         available=True),
                    Seat(label='C21',
                         top_position=59,
                         left_position=76,
                         available=True),
                    Seat(label='C22',
                         top_position=63,
                         left_position=76,
                         available=True),
                    Seat(label='C23',
                         top_position=55,
                         left_position=80,
                         available=True),
                    Seat(label='C24',
                         top_position=59,
                         left_position=80,
                         available=True),
                    Seat(label='C25',
                         top_position=63,
                         left_position=80,
                         available=True),
                    Seat(label='C26',
                         top_position=55,
                         left_position=84,
                         available=True),
                    Seat(label='C27',
                         top_position=59,
                         left_position=84,
                         available=True),
                    Seat(label='C28',
                         top_position=63,
                         left_position=84,
                         available=True),
                    Seat(label='C29',
                         top_position=57,
                         left_position=89,
                         available=True),
                    Seat(label='C30',
                         top_position=57,
                         left_position=92,
                         available=True),
                    Seat(label='C31',
                         top_position=57,
                         left_position=95,
                         available=True),
                    Seat(label='C32',
                         top_position=64,
                         left_position=89,
                         available=True),
                    Seat(label='C33',
                         top_position=64,
                         left_position=92,
                         available=True),
                    Seat(label='C34',
                         top_position=64,
                         left_position=95,
                         available=True)
                ]),
          Floor(number='4',
                map_image_url='images/Milstein_Floors/MLC_4th.png',
                seats=[
                    Seat(label='D1',
                         top_position=32,
                         left_position=12,
                         available=True),
                    Seat(label='D2',
                         top_position=32,
                         left_position=16,
                         available=True),
                    Seat(label='D3',
                         top_position=32,
                         left_position=22,
                         available=True),
                    Seat(label='D4',
                         top_position=32,
                         left_position=26,
                         available=True),
                    Seat(label='D5',
                         top_position=32,
                         left_position=32,
                         available=True),
                    Seat(label='D6',
                         top_position=32,
                         left_position=36,
                         available=True),
                    Seat(label='D7',
                         top_position=32,
                         left_position=42,
                         available=True),
                    Seat(label='D8',
                         top_position=32,
                         left_position=46,
                         available=True),
                    Seat(label='D9',
                         top_position=44,
                         left_position=25,
                         available=True),
                    Seat(label='D10',
                         top_position=44,
                         left_position=28,
                         available=True),
                    Seat(label='D11',
                         top_position=44,
                         left_position=33,
                         available=True),
                    Seat(label='D12',
                         top_position=44,
                         left_position=36,
                         available=True),
                    Seat(label='D13',
                         top_position=42,
                         left_position=53,
                         available=True),
                    Seat(label='D14',
                         top_position=42,
                         left_position=56,
                         available=True),
                    Seat(label='D15',
                         top_position=48,
                         left_position=53,
                         available=True),
                    Seat(label='D16',
                         top_position=48,
                         left_position=56,
                         available=True)
                ])
      ])
  db.session.add(Milstein)

  Avery = Library(name='Avery',
                  floors=[
                      Floor(number='1',
                            map_image_url='images/Avery_Floors/Avery_1st.png',
                            seats=[
                                Seat(label='A1',
                                     top_position=10,
                                     left_position=10,
                                     available=True),
                                Seat(label='A2',
                                     top_position=20,
                                     left_position=20,
                                     available=True),
                                Seat(label='A3',
                                     top_position=30,
                                     left_position=30,
                                     available=True),
                                Seat(label='A4',
                                     top_position=40,
                                     left_position=40,
                                     available=True)
                            ]),
                      Floor(number='2',
                            map_image_url='images/Avery_Floors/Avery_2nd.png',
                            seats=[
                                Seat(label='B1',
                                     top_position=10,
                                     left_position=10,
                                     available=True),
                                Seat(label='B2',
                                     top_position=20,
                                     left_position=20,
                                     available=True),
                                Seat(label='B3',
                                     top_position=30,
                                     left_position=30,
                                     available=True),
                                Seat(label='B4',
                                     top_position=40,
                                     left_position=40,
                                     available=True)
                            ]),
                      Floor(number='3',
                            map_image_url='images/Avery_Floors/Avery_3rd.png',
                            seats=[
                                Seat(label='C1',
                                     top_position=10,
                                     left_position=10,
                                     available=True),
                                Seat(label='C2',
                                     top_position=20,
                                     left_position=20,
                                     available=True),
                                Seat(label='C3',
                                     top_position=30,
                                     left_position=30,
                                     available=True),
                                Seat(label='C4',
                                     top_position=40,
                                     left_position=40,
                                     available=True)
                            ])
                  ])
  db.session.add(Avery)

  Uris = Library(name='Uris',
                 floors=[
                     Floor(number='1',
                           map_image_url='images/Uris_Floors/Uris_1st.png',
                           seats=[
                               Seat(label='A1',
                                    top_position=10,
                                    left_position=10,
                                    available=True),
                               Seat(label='A2',
                                    top_position=20,
                                    left_position=20,
                                    available=True),
                               Seat(label='A3',
                                    top_position=30,
                                    left_position=30,
                                    available=True),
                               Seat(label='A4',
                                    top_position=40,
                                    left_position=40,
                                    available=True)
                           ]),
                     Floor(number='2',
                           map_image_url='images/Uris_Floors/Uris_2nd.png',
                           seats=[
                               Seat(label='B1',
                                    top_position=10,
                                    left_position=10,
                                    available=True),
                               Seat(label='B2',
                                    top_position=20,
                                    left_position=20,
                                    available=True),
                               Seat(label='B3',
                                    top_position=30,
                                    left_position=30,
                                    available=True),
                               Seat(label='B4',
                                    top_position=40,
                                    left_position=40,
                                    available=True)
                           ])
                 ])
  db.session.add(Uris)

  db.session.commit()


def get_available_seats(library_name):
  library = Library.query.filter_by(name=library_name).first()
  if not library:
    return f"No library found with the name {library_name}"

  result = db.session.query(Floor.number, db.func.count(Seat.id)).join(
      Floor, Library.floors).join(Seat, Floor.seats).filter(
          Library.id == library.id,
          Seat.available == True).group_by(Floor.number).all()

  return {floor_number: count for floor_number, count in result}


def get_floor_image_url(library_name, floor_number):
  # Step 1: Find the library by name
  library = Library.query.filter_by(name=library_name).first()
  if not library:
    return f"No library found with the name {library_name}"

  # Step 2: Find the specified floor in the library
  floor = Floor.query.filter_by(library_id=library.id,
                                number=floor_number).first()
  if not floor:
    return f"No floor with number {floor_number} found in library {library_name}"

  # Step 3: Return the map image URL for the floor
  return floor.map_image_url


def get_seats_for_floor(library_name, floor_number):
  library = Library.query.filter_by(name=library_name).first()
  if not library:
    return f"No library found with the name {library_name}"

  floor = Floor.query.filter_by(library_id=library.id,
                                number=floor_number).first()
  if not floor:
    return f"No floor with number {floor_number} found in library {library_name}"

  seats = Seat.query.filter_by(floor_id=floor.id).all()

  # Formatting the result
  seat_details = [{
      'label': seat.label,
      'top_position': seat.top_position,
      'left_position': seat.left_position,
      'available': seat.available
  } for seat in seats]

  return seat_details


@app.route('/')
def index():
  return render_template('index.html')  # Ensure this template has the form


@app.route('/login')
def login():
  return render_template('login.html')


@app.route('/submit_form', methods=['POST'])
def submit_form():
  if request.method == 'POST':
    name = request.form['name']
    uni = request.form['uni']
    class_year = request.form['classYear']
    # Now you can store the data
    with open('userdata.txt', 'a') as file:
      file.write(f'{name},{uni},{class_year}\n')  # Simple CSV formats

    return jsonify({'success': True})


@app.route('/library-selection')
def library_selection():
  # Your logic here
  all_libraries = Library.query.all()
  return render_template('library_selection.html', libraries=all_libraries)


@app.route('/floor-capacity/<library_name>')  # Note the change here
def library_floor_capacity(library_name):
  print(library_name)
  floor_info = get_available_seats(library_name=library_name)
  print(floor_info)
  if not floor_info:
    return "Library not found", 404
  return render_template('floor_capacity.html',
                         library_name=library_name,
                         floors=floor_info)


@app.route('/pick-seat/<library_name>/<floor_number>')
def pick_seat(library_name, floor_number):
  # You could fetch the floor map image and seat details from the database here
  seat_info = get_seats_for_floor(library_name=library_name,
                                  floor_number=floor_number)

  floor_img_url = get_floor_image_url(library_name=library_name,
                                      floor_number=floor_number)

  return render_template('pick_seat.html',
                         library_name=library_name,
                         floor_name=floor_number,
                         floor_img_url=floor_img_url,
                         seats=seat_info)


@app.route('/select-timeslot/<libraryName>/<floorName>/<selectedSeatId>')
def select_timeslot(libraryName, floorName, selectedSeatId):

  return render_template('select_timeslot.html',
                         library_name=libraryName,
                         floor_name=floorName,
                         seat_id=selectedSeatId)


@app.route('/confirm-reservation', methods=['GET', 'POST'])
def confirm_reservation():
  if request.method == 'POST':
    session['library_name'] = request.form.get('library_name')
    session['floor_name'] = request.form.get('floor_name')
    session['seat_number'] = request.form.get('seat_id')
    session['start_time'] = request.form.get('start_time')
    session['end_time'] = request.form.get('end_time')
    session.modified = True
    print(session)
    # Redirect to the confirmation route
    return redirect(url_for('confirmation'))
    # return render_template('confirmation')


@app.route('/confirmation')
def confirmation():
  # Access the data from the session
  print(f"1:{session}")  # Debug: Print the whole session

  confirmation_data = {
      'library_name': session.get('library_name'),
      'floor_name': session.get('floor_name'),
      'seat_number': session.get('seat_number'),
      'start_time': session.get('start_time'),
      'end_time': session.get('end_time')
  }
  # print(confirmation_data)  # Debug: Print the data to be sent to the template

  # Render the confirmation page with the data
  return render_template('confirmation.html', **confirmation_data)


# @app.route('/confirm-reservation', methods=['GET', 'POST'])
# def confirm_reservation():
#   start_time = request.form.get('start_time')
#   end_time = request.form.get('end_time')
#   # Additional logic to process the reservation
#   return render_template('confirmation.html',
#                          start_time=start_time,
#                          end_time=end_time)


@app.route('/scan')
def scan():
  return render_template('scan.html')


@app.route('/home')
def home():
  seat_number = session.get('seat_number')
  current_time = session.get('start_time')
  end_time = session.get('end_time')

  return render_template('home.html',
                         seat_number=seat_number,
                         current_time=current_time,
                         end_time=end_time)


@app.route('/update-reservation', methods=['GET', 'POST'])
def update_reservation():
  seat_number = session.get('seat_number')
  current_end_time = session.get('end_time')
  return render_template('update_reservation.html',
                         seat_number=seat_number,
                         current_end_time=current_end_time)


@app.route('/confirmed', methods=['GET', 'POST'])
def confirmed():
  if request.method == 'POST':
    # Here you would extract the seat number and the new end time
    # from the form and process the update.
    seat_number = request.form.get('seat_number')
    updated_end_time = request.form.get('updated_end_time')
    session['end_time'] = updated_end_time
    session.modified = True
  return render_template('confirmed.html')


# @app.route('/update-seat-position', methods=['POST'])
# def update_seat_position():
#   data = request.get_json()
#   seat_id = data['id']
#   new_top = data['top']
#   new_left = data['left']

#   # Find the seat by ID and update its position
#   seat = Seat.query.filter_by(id=seat_id).first()
#   if seat:
#     seat.top_position = new_top
#     seat.left_position = new_left
#     db.session.commit()
#     return jsonify({'success': True})
#   return jsonify({'error': 'Seat not found'}), 404

if __name__ == '__main__':
  with app.app_context():
    db.drop_all()
    db.create_all()
    insert_seats()

  app.run(host='0.0.0.0', port=83, debug=True)
