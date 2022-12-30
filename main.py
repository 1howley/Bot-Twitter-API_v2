import tweepy
import random
from time import sleep

consumer_key = "API KEY"
consumer_secret = "API KEY SECRET"
access_token = "ACESS TOKEN"
access_token_secret = "ACESS TOKEN SECRET"

client = tweepy.Client(
    consumer_key="API KEY", consumer_secret="API KEY SECRET",
    access_token="ACESS TOKEN", access_token_secret="ACESS TOKEN SECRET"
)


def sorteador():
    a1 = "O Neymar"
    a2 = "O Cristiano Ronaldo"
    a3 = "O Messi"
    a4 = "O Mbappé"

    b1 = " nunca foi"
    b2 = " já foi"
    b3 = " jamais será"
    b4 = " é"

    c1 = " um craque e extremamente decisivo"
    c2 = " bom, hoje o futebol não precisa mais dele"
    c3 = " um jogador de porte para grandes clubes"
    c4 = " um pereba e não tem perna esquerda"

    subject = random.choice([a1, a2, a3, a4])
    tempo = random.choice([b1, b2, b3, b4])
    adjetivo = random.choice([c1, c2, c3, c4])


    frase = subject + tempo + adjetivo

    return frase


while True:
    try:
        response = client.create_tweet(text= sorteador())
        print("tweet feito!")
    except:
        print("Algo falhou :(")
        ready = False
    sleep(15)
