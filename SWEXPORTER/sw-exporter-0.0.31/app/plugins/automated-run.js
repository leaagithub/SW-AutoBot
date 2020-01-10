const requestLib = require('request');
const python_URL = 'http://127.0.0.1:5000/';
let request;
module.exports = {
  defaultConfig: {
    enabled: false
  },
  // plugin meta data to better describe your plugin
  pluginName: 'Automated Run',
  pluginDescription: 'This plugin shows you all API events in the log. Sends a response based on what API command it receives.',
  init(proxy, config) {
    // Subscribe to api command events from the proxy here.
    // You can subscribe to specifc API commands. Event name is the same as the command string
    request = requestLib.defaults({
      baseUrl: python_URL
    });
    proxy.on('HubUserLogin', () => {
      if (config.Config.Plugins[this.pluginName].enabled) {
        proxy.log({
          type: 'info',
          source: 'plugin',
          name: this.pluginName,
          message: 'You just logged into the game.'
        });
      }
    });
    // or all API commands with the 'apiCommand' event
    proxy.on('apiCommand', (req, resp) => {
      if (config.Config.Plugins[this.pluginName].enabled) {
        this.processEveryCommand(proxy, req, resp);
        console.log("RESP:   ");
        console.log(resp);
        const {
          command
        } = resp;
        switch (command) {
          case 'BattleDungeonResult':
            sendData(proxy,resp,command)
            break;
          case 'BattleTrialTowerResult_v2':
            sendData(proxy,resp,command)
            break;
          case 'BattleDimensionHoleDungeonResult':
            sendData(proxy,resp,command)
            break;
          case 'BattleRiftOfWorldsRaidResult':
            sendData(proxy,resp,command)
            break;
          case 'BattleRiftDungeonResult':
            sendData(proxy,resp,command)
            break;
          case 'battleGuildMazeResult':
            sendData(proxy,resp,command)
            break;
        }
      }
    });
  },
  processEveryCommand(proxy, req) {
    proxy.log({
      type: 'info',
      source: 'plugin',
      name: this.pluginName,
      message: `Found API Command ${req.command}`
    });
  }
};

function sendData(proxy,objectBody,dungeonType) {
  const req_options = {
    json: true,
    body: objectBody
  }
  dungeonType = dungeonType + '/'
  request.post(dungeonType, req_options, (error, response, body) => {
    if (error) {
      proxy.log({
        message: `Error: ${error.message}`
      });
      return;
    }
    if (response.statusCode === 200) {
      proxy.log({
        message: 'Successful Sent Response to Py Program.'
      })
    }
  })
}