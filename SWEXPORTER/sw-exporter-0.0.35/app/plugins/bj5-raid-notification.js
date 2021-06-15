const pluginName = 'BJ5RaidNotification';
const Discord = require('discord.js');
const webhook = new Discord.WebhookClient("846520413580296213", "KCXUxQTn9qvTRWg2mAkGRsxhqfBqedc11-d2Ml-6UBAOErZ7jVMJinyhvQaYgNiYjhm-");
raidcount = 0;

module.exports = {
  defaultConfig: {
    enabled: false,
    reset: false,
    raidpartner1: '',
    raidpartner2: '',
    raidpartner3: '',
    message: ''
  },
  defaultConfigDetails: {
    reset: {label: 'Reset RunCount to 0'},
    raidpartner1: { label: 'Discord ID of Raid Partner 1', type: 'input'},
    raidpartner2: { label: 'Discord ID of Raid Partner 2', type: 'input'},
    raidpartner3: { label: 'Discord ID of Raid Partner 3', type: 'input'},
    message: {label: 'Send Message', type: 'textarea'}
  },
  // plugin meta data to better describe your plugin
  pluginName: 'BJ5RaidNotification',
  pluginDescription: 'This plugin shows send discord notification after 10 runs of BJ5',
  init(proxy, config) {
    // Subscribe to api command events from the proxy here.
    // You can subscribe to specifc API commands. Event name is the same as the command string
    proxy.on('apiCommand', (req, resp) => {
      const {
        command
      } = resp;
      if (config.Config.Plugins[this.pluginName].enabled) {
        if (config.Config.Plugins[this.pluginName].reset){
          raidcount = 0;
        }
        switch (command) {
          case 'BattleRiftOfWorldsRaidResult':
            raidcount += 1;
            if (raidcount == 10){
              let mesContent = '';
              console.log(config.Config.Plugins[pluginName].raidpartner1);
              if(config.Config.Plugins[pluginName].raidpartner1 !== ""){
                mesContent += '<@' + config.Config.Plugins[pluginName].raidpartner1 + '> ';
                console.log(mesContent);
              }
              if(config.Config.Plugins[pluginName].raidpartner2 !== ""){
                mesContent += '<@' + config.Config.Plugins[pluginName].raidpartner2 + '> ';
                console.log(mesContent);
              }
              if(config.Config.Plugins[pluginName].raidpartner3 !== ""){
                mesContent += '<@' + config.Config.Plugins[pluginName].raidpartner3 + '> ';
                console.log(mesContent);
              }
              if(!config.Config.Plugins[pluginName].message!== ""){
                mesContent += config.Config.Plugins[pluginName].message;
              }
              webhook.send(mesContent)
                .catch(console.error);
              console.log(mesContent);
              console.log('Done');
              raidcount = 0;
            }
          console.log('Run Count', raidcount);
          break;
        }
      }
    });
  },  
};