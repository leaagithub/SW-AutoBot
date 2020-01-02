module.exports = {
  defaultConfig: {
    enabled: true
  },
  pluginName: 'Sell-Response-Plugin',
  pluginDescription: 'Tells you if a rune is worth keeping or not.',
  init(proxy) {
    proxy.on('apiCommand', (req, resp) => {
      if (config.Config.Plugins[this.pluginName].enabled) {
        this.processCommand(proxy, req, resp);
      }
    });
  },
  processCommand(proxy, req, resp) {
    const { command } = req;
    let runesInfo = [];

    // Extract the rune and display it's efficiency stats.
    switch (command) {
      case 'BattleDungeonResult':
      case 'BattleScenarioResult':
      case 'BattleDimensionHoleDungeonResult':
        if (resp.win_lose === 1) {
          const reward = resp.reward ? resp.reward : {};

          if (reward.crate && reward.crate.rune) {
            runesInfo.push(this.logRuneDrop(reward.crate.rune));
          }
        }
        break;
      case 'UpgradeRune': {
        const originalLevel = req.upgrade_curr;
        const newLevel = resp.rune.upgrade_curr;

        if (newLevel > originalLevel && newLevel % 3 === 0 && newLevel <= 12) {
          runesInfo.push(this.logRuneDrop(resp.rune));
        }
        break;
      }
      case 'AmplifyRune':
      case 'ConfirmRune':
        runesInfo.push(this.logRuneDrop(resp.rune));
        break;

      case 'BuyBlackMarketItem':
        if (resp.runes && resp.runes.length === 1) {
          runesInfo.push(this.logRuneDrop(resp.runes[0]));
        }
        break;

      case 'BuyGuildBlackMarketItem':
        if (resp.runes && resp.runes.length === 1) {
          runesInfo.push(this.logRuneDrop(resp.runes[0]));
        }
        break;

      case 'BuyShopItem':
        if (resp.reward && resp.reward.crate && resp.reward.crate.runes) {
          runesInfo.push(this.logRuneDrop(resp.reward.crate.runes[0]));
        }
        break;

      case 'GetBlackMarketList':
        resp.market_list.forEach(item => {
          if (item.item_master_type === 8 && item.runes) {
            runesInfo.push(this.logRuneDrop(item.runes[0]));
          }
        });
        break;

      case 'GetGuildBlackMarketList':
        resp.market_list.forEach(item => {
          if (item.item_master_type === 8 && item.runes) {
            runesInfo.push(this.logRuneDrop(item.runes[0]));
          }
        });
        break;

      case 'BattleWorldBossResult': {
        const reward = resp.reward ? resp.reward : {};

        if (reward.crate && reward.crate.runes) {
          reward.crate.runes.forEach(rune => {
            runesInfo.push(this.logRuneDrop(rune));
          });
        }
        break;
      }
      case 'BattleRiftDungeonResult':
        if (resp.item_list) {
          resp.item_list.forEach(item => {
            if (item.type === 8) {
              runesInfo.push(this.logRuneDrop(item.info));
            }
          });
        }
        break;

      default:
        break;
    }

    if (runesInfo.length > 0) {
      proxy.log({
        type: 'info',
        source: 'plugin',
        name: this.pluginName,
        message: this.mountRuneListHtml(runesInfo)
      });
    }
  },

  logRuneDrop(rune) {
    const efficiency = gMapping.getRuneEfficiency(rune);
    const runeQuality = gMapping.rune.quality[rune.rank];
    const colorTable = {
      Common: 'grey',
      Magic: 'green',
      Rare: 'blue',
      Hero: 'purple',
      Legend: 'orange'
    };

    let color = colorTable[runeQuality];
    let runeClass = gMapping.isAncient(rune) ? rune.class - 10 : rune.class;
    if ((runeClass == 6 && color == orange)||(runeClass == 6 && color == purple)){
		return '<img src="../assets/icons/sell-pic.png" />'; 
	}
	else {
		return '<img src="../assets/icons/sell-pic.png" />'; 
	}
  }
};
