const Discord = require('discord.js');
const client = new Discord.Client();

client.on('ready', ()=> {
    console.log('Mira est Ok.')
});
client.on('message', message => {
    if message.content === 'ping') {
        message.reply('pong');   
    }
    
});
                
client.login('NDI2ODUxMTMyODIwOTQ2OTQ1.DZcH2Q.AqhM4vfkS2CCFgNsWv3T9iNeeuY');
