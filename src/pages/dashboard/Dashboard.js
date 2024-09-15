import "./Dashboard.css";
import { Card } from "../../components";

const Dashboard = () => {
  return (
    <div className="dashboard">
      <div class="dashboard-app-header">
        <h1>Ready to lock in?</h1>
        <a href="/profile">profile</a>
      </div>
      <Card>
        <div className="ted-status">
          <div className="circle"></div>
          <h2 className="card-title">TED is ready</h2>
        </div>
        <a href="/">chat</a>
      </Card>
      <Card id="current-session">
        <h2>Session length</h2>
        <div className="current-session-info">
          <div className="session-length-display">
            <button>-</button>
            <h3>90 mins</h3>
            <button>+</button>
          </div>
        </div>
        <div className="session-length-options">
          <button>30</button>
          <button>60</button>
          <button>90</button>
          <button>120</button>
        </div>
      </Card>
    </div>
  );
};

export default Dashboard;
