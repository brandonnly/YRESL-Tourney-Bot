const Discord = require('discord.js');
const client = new Discord.Client();
const prefix = 'yr!';
const fs = require('fs');

client.commands = new Discord.Collection();

const commandFiles = fs.readdirSync('./commands/').filter(file => file.endsWith('.js'));
for (const file of commandFiles) {
    const command = require(`./commands/${file}`);

    client.commands.set(command.name, command);
}

client.once('ready', () => {
    console.log('YRESL bot is online!')
    client.guilds.cache.forEach((guild) => {
        client.user.setActivity(`YRESL Bot || yr!`);
    })

});

client.on('message', message => {
    if (!message.content.startsWith(prefix) || message.author.bot) return;

    const args = message.content.slice(prefix.length).split(/ +/);
    const command = args.shift().toLowerCase();

    if (command === 'team') {
        client.commands.get("team").execute("message, args, client, Discord, prefix")
    }

});


client.login('');