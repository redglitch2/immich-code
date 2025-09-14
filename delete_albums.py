import requests

# -------------------
# CONFIG
# -------------------
IMMICH_URL = ""
API_KEY = ""  # <-- paste your API key here

headers = {
    "x-api-key": API_KEY,
    "Content-Type": "application/json"
}


def list_albums():
    """Fetch all albums from Immich"""
    resp = requests.get(f"{IMMICH_URL}/albums", headers=headers)
    resp.raise_for_status()
    return resp.json()

def delete_album(album_id, album_name=""):
    """Delete an album by ID"""
    resp = requests.delete(f"{IMMICH_URL}/albums/{album_id}", headers=headers)
    if resp.status_code == 204:
        print(f"✅ Deleted album: {album_name} ({album_id})")
    else:
        print(f"❌ Failed to delete {album_name} ({album_id}) -> {resp.status_code}: {resp.text}")

def main():
    albums = list_albums()
    print(f"Found {len(albums)} albums")

    for album in albums:
        album_id = album["id"]
        album_name = album.get("albumName", "Unnamed")
        delete_album(album_id, album_name)

if __name__ == "__main__":
    main()
