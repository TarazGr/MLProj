from joblib import dump, load
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
import pandas as pd

clf = load("DTree_Model.joblib")

client_credentials_manager = SpotifyClientCredentials("75d944d4a2f64af3ada75b8d846451a8",
                                                      "399a7ee3bdc947b799148755314b4753")
spotify = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
