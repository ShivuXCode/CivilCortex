import json
import urllib.parse
from http.server import BaseHTTPRequestHandler, HTTPServer
from agents.agent1_condition import assess_condition
from agents.agent2_risk import assess_risk
from agents.agent3_priority import assess_priority
from agents.agent4_planning import plan_maintenance
from agents.agent5_resources import optimize_resources
from agents.agent6_llm import generate_recommendation

class CivilCortexHandler(BaseHTTPRequestHandler):
    def _set_headers(self, status=200):
        self.send_response(status)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'X-Requested-With, Content-type')
        self.end_headers()

    def do_OPTIONS(self):
        self._set_headers()
        self.wfile.write(b"")

    def do_POST(self):
        parsed_path = urllib.parse.urlparse(self.path)
        
        if parsed_path.path == '/api/analyze-maintenance':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            
            try:
                req_json = json.loads(post_data)
                
                # 1. Initialize State from Module 1 & 2 Inputs
                state = {
                    # Module 1 (Crack & Defect Detection)
                    "crack_type": req_json.get("crack_type", ""),
                    "defect": req_json.get("defect", ""),
                    "severity": req_json.get("severity", "medium"),
                    
                    # Module 2 (Construction Analytics)
                    "helmet_compliance": float(req_json.get("helmet_compliance", 100)),
                    "vest_compliance": float(req_json.get("vest_compliance", 100)),
                    "expected_progress": float(req_json.get("expected_progress", 100)),
                    "actual_progress": float(req_json.get("actual_progress", 100)),
                    "utilization": float(req_json.get("utilization", 100)),
                    "delay_risk": req_json.get("delay_risk", "low")
                }
                
                # 2. Execute 6-Agent Pipeline
                state.update(assess_condition(state))      # Agent 1
                state.update(assess_risk(state))           # Agent 2
                state.update(assess_priority(state))       # Agent 3
                state.update(plan_maintenance(state))      # Agent 4
                state.update(optimize_resources(state))    # Agent 5
                state.update(generate_recommendation(state)) # Agent 6
                
                # 3. Return Final State
                self._set_headers(200)
                self.wfile.write(json.dumps(state).encode('utf-8'))
                
            except Exception as e:
                self._set_headers(400)
                error_msg = {"error": str(e)}
                self.wfile.write(json.dumps(error_msg).encode('utf-8'))
        else:
            self._set_headers(404)
            self.wfile.write(b'{"error": "Not Found"}')

def run(server_class=HTTPServer, handler_class=CivilCortexHandler, port=8000):
    server_address = ('127.0.0.1', port)
    httpd = server_class(server_address, handler_class)
    print(f"Starting standard HTTP server on 127.0.0.1:{port}...")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    print("Server stopped.")

if __name__ == '__main__':
    run()
