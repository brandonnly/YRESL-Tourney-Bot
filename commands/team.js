module.exports = {
    name: 'team',
    description: "Team Matchmaking",
    execute(message, args, Discord, prefix) {
        const val_category_id = '829803831767334932';
        const lol_category_id = '829803675308130315';
        const guild_id = '822264218492862504';
        const exec_role_id = '822264218546864134';
        const Embed = new Discord.Embed()
            .setAuthor("YRESL Bot", "https://image.brandonly.me/yresllogo.png", "https://yresl.ca/")
            .setFooter("YRESL April Break 2021 Tournaments || YRESL Bot Prefix: " + prefix)
        const GameType = message.content.split(' ')[1];
        const Team_Members = message.content.split('=+=')[2];
        const Team_MembersList = message.content.split(' ')[2];


        if (GameType = '') {
            Embed.addField('Please specify a game type. ("val" or "lol")')
        }

        if (Team_Members = '') {
            Embed.addField('Please specify the team members.')
        }
        message.guild.roles.create({
            data: {
                name: 'Owner',
                color: 'YELLOW',
                permissions: [AdminP, ServerMP],
            },
            reason: 'we needed a role for Super Cool People',
        });

        Team_Members.forEach(function (Member) {
            console.log(Member);
            if (Team_Members = message.guild.members.toLowerCase().cache.find(Team_Members.displayName)) {

            }

        });

    }
}