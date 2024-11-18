import spotipy
from spotipy.oauth2 import SpotifyOAuth
from ytmusicapi import YTMusic

# inicializa o Youtube Music com os cookies
ytmusic = YTMusic(r'caminho-para-seu-arquivo-browser.json')


# informações do aplicativo no Spotify Developer
client_id = "seu-id-aqui"
client_secret = "sua-senha-aqui"
redirect_uri = "seu-URI-aqui"
# define o escopo de permissões do Spotify
scope = "playlist-read-private"
# configuração de autenticação do Spotify
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri, scope=scope))


# busca todas as playlists no Spotify do usuário
playlists = sp.current_user_playlists() 



# a função certifica se uma playlist com o mesmo nome já existe, e retorna seu ID caso já exista:
def find_existing_playlist(ytmusic, playlist_name):
    playlists = ytmusic.get_library_playlists()
    for playlist in playlists:
        if playlist['title'] == playlist_name:
            return playlist['playlistId']
    return None



# A API do Spotify permite buscar no máximo 100 músicas por playlist, essa função contorna esse problema
def get_all_tracks_from_playlist(sp, playlist_id):
    tracks = []
    offset = 0
    limit = 100 
    
    while True:
        response = sp.playlist_tracks(sp_playlist_id, limit=limit, offset=offset)
        tracks.extend(response['items'])

        if len(response['items']) < limit:
            break
        
        offset += limit
    return tracks



for playlist in playlists['items']:

    # verifica se a playlist já existe no YT Music
    playlist_name = playlist['name']

    yt_playlist_id = find_existing_playlist(ytmusic, playlist_name)
    if yt_playlist_id:
        print(f"\nPlaylist '{playlist_name}' já existente, adicionando músicas restantes.")
    else:         
        # criação da playlist no Youtube Music
        yt_playlist_id = ytmusic.create_playlist(
            
            title=playlist['name'],
            description='',
            privacy_status="PUBLIC"
        )
        print(f"\nPlaylist: '{playlist['name']}' criada com o ID: {yt_playlist_id}\n")

    print("-" * 50 + "\n")


    # busca todas as músicas da playlist no Spotify
    sp_playlist_id = playlist['id']
    tracks = get_all_tracks_from_playlist(sp, sp_playlist_id)

    # busca as músicas da playlist no YT Music
    yt_playlist_tracks = ytmusic.get_playlist(yt_playlist_id, limit=500)['tracks']
    yt_track_titles = set(
        f"{track['title']} - {', '.join(artist['name'] for artist in track['artists'])}" for track in yt_playlist_tracks
    )

    for track_item in tracks:
        track = track_item['track']
        track_name = track['name']
        artists = ', '.join(artist['name'] for artist in track['artists'])
                
        # cria uma string com o nome da música e do artista
        track_search = track_name +  " - " + artists
       
        if track_search in yt_track_titles:
            # verifica se a música já está na playlist
            print(f"Música '{track_name}' já está na playlist.")
      
        else: 
            # pesquisa a música e adiciona a playlist se ela for encontrada
            search_result = ytmusic.search(track_search, filter="songs")
            if search_result:
                song_id = search_result[0]['videoId']
                ytmusic.add_playlist_items(yt_playlist_id, [song_id])
                print(f"Música: {track_name} --- Adicionada a playlist {playlist['name']}")
            else:
                print(f"Erro ao adicionar a música: {track_name}")
