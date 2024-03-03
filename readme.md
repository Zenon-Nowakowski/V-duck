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
pip install discord pynacl
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
- Responds to @ mentions
# TODO
- Meme implementation 
   - Copy pasta command
- Voice filtering 
   - Intake user voice and timeout users who say certain words
- Better dice rolling (modifiers and giving totals)
- Media player
- Reply to @'s
   - insults you 
- Improve filtering
   - remove excessive lettering 
   - remove excess spacing exploit 
- Polling
- React rolls 