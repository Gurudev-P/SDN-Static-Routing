from ryu.base import app_manager
from ryu.controller import ofp_event
from ryu.controller.handler import CONFIG_DISPATCHER
from ryu.controller.handler import set_ev_cls
from ryu.ofproto import ofproto_v1_3

class StaticRouting(app_manager.RyuApp):
    OFP_VERSIONS = [ofproto_v1_3.OFP_VERSION]

    def add_flow(self, datapath, priority, match, actions):
        ofproto = datapath.ofproto
        parser = datapath.ofproto_parser

        inst = [parser.OFPInstructionActions(ofproto.OFPIT_APPLY_ACTIONS, actions)]
        mod = parser.OFPFlowMod(
            datapath=datapath,
            priority=priority,
            match=match,
            instructions=inst
        )
        datapath.send_msg(mod)

    @set_ev_cls(ofp_event.EventOFPSwitchFeatures, CONFIG_DISPATCHER)
    def switch_features_handler(self, ev):
        dp = ev.msg.datapath
        parser = dp.ofproto_parser

        print("Switch connected:", dp.id)

        if dp.id == 1:
            self.add_flow(dp, 1, parser.OFPMatch(in_port=1),
                          [parser.OFPActionOutput(2)])
            self.add_flow(dp, 1, parser.OFPMatch(in_port=2),
                          [parser.OFPActionOutput(1)])

        elif dp.id == 2:
            self.add_flow(dp, 1, parser.OFPMatch(in_port=1),
                          [parser.OFPActionOutput(2)])
            self.add_flow(dp, 1, parser.OFPMatch(in_port=2),
                          [parser.OFPActionOutput(1)])
