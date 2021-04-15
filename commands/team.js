const { Team } = require("discord.js");

module.exports = {
    name: 'team',
    description: "Team Matchmaking",
    execute(message, args, Discord, prefix) {
        const Embed = new Discord.Embed()
            .setAuthor("YRESL Bot", "https://image.brandonly.me/yresllogo.png", "https://yresl.ca/")
            .setFooter("YRESL April Break 2021 Tournaments || YRESL Bot Prefix: " + prefix)
        const GameType = message.content.split(' ')[1];
        const Team_Members = message.content.split('=+=')[2]
        
        if (GameType = '') {
            Embed.addField('Please specify a game type. ("val" or "lol")')
        }
        if (Team_Members = '') {
            Embed.addField('Please specify the team members.')
        }
        Team_Members.forEach(function(Member) {
            console.log(Member);
        });
    }
}