# :V
A silly discord bot for personal use. 

# Installation
1. Clone the repository:
   ```shell
   git clone https://github.com/your-username/your-repo.git
   ```
2. Set up copypasta.json and internal.json 
The format for the copypasta.json is: 
```json
{
"copyastas":
[
    {
        "name": "Own a musket for home defense",
        "text": "Own a musket for home defense false Own a musket for home defense, since that's what the founding fathers intended. Four ruffians break into my house. 'What the devil?' As I grab my powdered wig and Kentucky rifle. Blow a golf ball sized hole through the first man, he's dead on the spot. Draw my pistol on the second man, miss him entirely because it's smoothbore and nails the neighbors dog. I have to resort to the cannon mounted at the top of the stairs loaded with grape shot, 'Tally ho lads' the grape shot shreds two men in the blast, the sound and extra shrapnel set off car alarms. Fix bayonet and charge the last terrified rapscallion. He Bleeds out waiting on the police to arrive since triangular bayonet wounds are impossible to stitch up. Just as the founding fathers intended."
    }
]
}
```
whereas the format for the internal.json file is: 
```json

{"token": "mytoken",
"filtered_strings":["filter1", "filter2", "filter3", "etc"]}
```
## Dependencies 
The bot requires the following dependencies: 
```shell 
pip install discord pynacl pytube ffmpeg
```
### Additional dependency notes
You will need to download ffmpeg in addition to the library 
# Running remotly 
If you plan on running this bot on a raspi here is the SSH command to let it run indefinatly, as well as shutting it down. I reccommend tmux for session hosting, like so.
```shell
tmux new -s bot
tmux detach
```
reconnect with: 
```shell
tmux a -t bot
```
# Features 
- Word filtering: 
   - In the internal.json file there shoud be a filtered_strings array, which will be read and any message containing a filtered word will result in an automatic timeout. 
   - Filtering is prossessed through filteralg.py and must be similar by a factor of 80% to the filter list in order to be filtered. 
- Dice rolling 
   - Simple NdN format
- echo 
   - the echo command will, echo, whatever the string following the command is 
- leave/join 
   - can join and leave voicecall (essentially subcommands code for use in more complex systems such as the play command)
- Responds to @ mentions (currently very limited)
- Copypasta
   - A user may ask the bot to provide a copypasta from internals
- play audio
   - currently very buggy, needs more testing. 
# TODO
- Meme implementation 
   - Better copy pasta generation (api/web)
   - Generate memes dynamically 
- Voice filtering 
   - Intake user voice and timeout users who say certain words
- Better dice rolling (modifiers and giving totals)
- Media player
   - Fix audio queuing 
- Reply to @'s more dynamically
   - Chat bot, most likely utilizing Googles Gemini
- Improve filtering
   - remove excessive lettering 
   - remove excess spacing exploit 
- Polling
- React rolls 
- Image identification 
   - Connect to API of bannable images 
   - Create a ML algorithm to identify pictures and timeout users for posting them
- Play Uno
   - Turn order 
   - Player hands 
   - Draw cards 
- Play tik-tak-toe