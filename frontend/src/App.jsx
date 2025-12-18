import React, { useState, useEffect } from 'react';
import {
    Activity,
    Map as MapIcon,
    Users,
    ShieldAlert,
    Brain,
    MessageSquare,
    Terminal,
    Zap,
    Droplets,
    Sun,
    AlertTriangle
} from 'lucide-react';
import { motion, AnimatePresence } from 'framer-motion';

const App = () => {
    const [activeTab, setActiveTab] = useState('command');
    const [logs, setLogs] = useState([
        { id: 1, text: "System Initializing...", type: "system" },
        { id: 2, text: "GeoSentinel: Scanning Garissa Sub-counties...", type: "geo" },
        { id: 3, text: "LogicCore: Bayesian Priors loaded from MOH 2024 data.", type: "logic" }
    ]);
    const [patientIndex, setPatientIndex] = useState(0);

    // Simulated live feed effect
    useEffect(() => {
        const interval = setInterval(() => {
            const messages = [
                "TriageBot: Processing P-82910 from Dadaab...",
                "GeoSentinel: Thermal anomaly detected in Balambala.",
                "LogicCore: High correlation between flood data and febrile symptoms.",
                "EthicsGuard: Patient privacy filter applied.",
                "System: Batch REAL-STATS-SIM-2024 sync in progress..."
            ];
            const newMsg = {
                id: Date.now(),
                text: messages[Math.floor(Math.random() * messages.length)],
                type: "auto"
            };
            setLogs(prev => [newMsg, ...prev].slice(0, 50));
        }, 4000);
        return () => clearInterval(interval);
    }, []);

    return (
        <div className="dashboard-container">
            <div className="main-grid">

                {/* SIDEBAR NAVIGATION */}
                <aside className="glass-panel sidebar">
                    <div style={{ padding: '0 12px 20px 12px' }}>
                        <div className="title-glow">AFYADOCTOR</div>
                        <div style={{ fontSize: '0.7rem', color: 'var(--primary)', letterSpacing: '4px' }}>ANTIGRAVITY v3.0</div>
                    </div>

                    <nav>
                        <NavItem icon={<Activity size={20} />} label="Command Center" active={activeTab === 'command'} onClick={() => setActiveTab('command')} />
                        <NavItem icon={<MapIcon size={20} />} label="GeoSentinel Map" active={activeTab === 'map'} onClick={() => setActiveTab('map')} />
                        <NavItem icon={<Users size={20} />} label="Patient Registry" active={activeTab === 'patients'} onClick={() => setActiveTab('patients')} />
                        <NavItem icon={<Brain size={20} />} label="Hive Mind Logs" active={activeTab === 'hive'} onClick={() => setActiveTab('hive')} />
                        <NavItem icon={<MessageSquare size={20} />} label="Baraza Advisory" active={activeTab === 'advisory'} onClick={() => setActiveTab('advisory')} />
                    </nav>

                    <div style={{ marginTop: 'auto', paddingTop: '2rem' }}>
                        <div className="community-card">
                            <div style={{ display: 'flex', alignItems: 'center', gap: '8px', marginBottom: '10px' }}>
                                <Zap size={16} color="var(--primary)" />
                                <span style={{ fontSize: '0.8rem', fontWeight: 600 }}>SYSTEM STATUS</span>
                            </div>
                            <div style={{ fontSize: '0.7rem', color: 'var(--text-muted)' }}>
                                Gemini 1.5 Flash: <span style={{ color: 'var(--primary)' }}>ONLINE</span><br />
                                GEE Sentinel: <span style={{ color: 'var(--primary)' }}>ACTIVE</span><br />
                                Inference Latency: 420ms
                            </div>
                        </div>
                    </div>
                </aside>

                {/* MAIN CONTENT AREA */}
                <main style={{ display: 'flex', flex_direction: 'column', gap: '2rem' }}>

                    {/* TOP STATS */}
                    <div style={{ display: 'grid', gridTemplateColumns: 'repeat(3, 1fr)', gap: '1rem' }}>
                        <div className="glass-panel stats-card">
                            <div className="stats-label">Total Triage (24h)</div>
                            <div className="stats-value">2,410</div>
                        </div>
                        <div className="glass-panel stats-card" style={{ borderColor: 'var(--secondary)' }}>
                            <div className="stats-label">High Risk Alerts</div>
                            <div className="stats-value" style={{ color: 'var(--secondary)' }}>42</div>
                        </div>
                        <div className="glass-panel stats-card">
                            <div className="stats-label">Critical Malnutrition</div>
                            <div className="stats-value">IPC 4</div>
                        </div>
                    </div>

                    {/* DYNAMIC VIEW */}
                    <div className="glass-panel" style={{ flex: 1, position: 'relative' }}>
                        {activeTab === 'command' && (
                            <motion.div initial={{ opacity: 0 }} animate={{ opacity: 1 }}>
                                <h2 style={{ marginBottom: '1.5rem', display: 'flex', alignItems: 'center', gap: '10px' }}>
                                    <ShieldAlert className="animate-pulse" color="var(--secondary)" /> Live Operations Feed
                                </h2>

                                <div className="map-placeholder">
                                    <div className="map-ui-overlay">
                                        COORD: 0.4532° S, 39.6461° E (GARISSA)<br />
                                        LAYER: INFECTIOUS_CLUSTERS_2024
                                    </div>
                                    {/* Simulated Map Visual */}
                                    <div style={{ width: '100%', height: '100%', background: 'linear-gradient(45deg, #0e0e12 25%, #15151b 25%, #15151b 50%, #0e0e12 50%, #0e0e12 75%, #15151b 75%, #15151b 100%)', backgroundSize: '40px 40px', opacity: 0.3 }}></div>
                                    <motion.div
                                        animate={{ scale: [1, 1.2, 1], opacity: [0.5, 0.8, 0.5] }}
                                        transition={{ duration: 3, repeat: Infinity }}
                                        style={{ position: 'absolute', top: '40%', left: '60%', width: '40px', height: '40px', borderRadius: '50%', background: 'radial-gradient(circle, var(--secondary), transparent)' }}
                                    />
                                    <motion.div
                                        animate={{ scale: [1, 1.5, 1], opacity: [0.4, 0.7, 0.4] }}
                                        transition={{ duration: 4, repeat: Infinity, delay: 1 }}
                                        style={{ position: 'absolute', top: '30%', left: '45%', width: '30px', height: '30px', borderRadius: '50%', background: 'radial-gradient(circle, var(--primary), transparent)' }}
                                    />
                                </div>

                                <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '1.5rem', marginTop: '2rem' }}>
                                    <div>
                                        <h3 style={{ fontSize: '0.9rem', marginBottom: '1rem', color: 'var(--text-muted)' }}>MOH STATISTICAL TRENDS (GARISSA)</h3>
                                        <div className="community-card" style={{ height: '150px' }}>
                                            {/* CSS-only Bar Chart */}
                                            <div style={{ display: 'flex', alignItems: 'flex-end', height: '100%', gap: '10px' }}>
                                                <div style={{ background: 'var(--primary)', width: '20%', height: '80%', borderRadius: '4px 4px 0 0' }}></div>
                                                <div style={{ background: 'var(--secondary)', width: '20%', height: '45%', borderRadius: '4px 4px 0 0' }}></div>
                                                <div style={{ background: 'var(--primary)', width: '20%', height: '90%', borderRadius: '4px 4px 0 0' }}></div>
                                                <div style={{ background: 'var(--secondary)', width: '20%', height: '60%', borderRadius: '4px 4px 0 0' }}></div>
                                                <div style={{ background: 'white', opacity: 0.1, width: '20%', height: '30%' }}></div>
                                            </div>
                                        </div>
                                    </div>
                                    <div>
                                        <h3 style={{ fontSize: '0.9rem', marginBottom: '1rem', color: 'var(--text-muted)' }}>PARTICIPATORY REPORT</h3>
                                        <div className="community-card">
                                            <p style={{ fontSize: '0.8rem', lineHeight: '1.4' }}>
                                                "The community in Fafi reports increased eye irritation. GEE confirms high PM2.5 (Dust) due to drought. <strong>Recommendation:</strong> Use protective eye gear and ensure children stay indoors during peak winds."
                                            </p>
                                        </div>
                                    </div>
                                </div>
                            </motion.div>
                        )}
                        {activeTab !== 'command' && <div style={{ padding: '4rem', textAlign: 'center', opacity: 0.5 }}>Module Loading... [Simulated Link Ready]</div>}
                    </div>
                </main>

                {/* RIGHT FEED (Hive Mind Logs) */}
                <aside className="glass-panel sidebar">
                    <h3 style={{ fontSize: '1rem', display: 'flex', alignItems: 'center', gap: '10px', marginBottom: '1rem' }}>
                        <Terminal size={18} color="var(--primary)" /> AGENTIC REASONING
                    </h3>
                    <div className="thinking-log">
                        <AnimatePresence initial={false}>
                            {logs.map(log => (
                                <motion.div
                                    key={log.id}
                                    initial={{ opacity: 0, x: 20 }}
                                    animate={{ opacity: 1, x: 0 }}
                                    className="log-entry"
                                >
                                    {log.text}
                                </motion.div>
                            ))}
                        </AnimatePresence>
                    </div>

                    <div style={{ marginTop: '2rem' }}>
                        <h3 style={{ fontSize: '0.9rem', marginBottom: '1rem' }}>ENVIRONMENTAL RISKS</h3>
                        <RiskItem icon={<Droplets size={16} />} label="Dadaab (Flood)" risk="MODERATE" color="#fbbf24" />
                        <RiskItem icon={<Sun size={16} />} label="Lagdera (Heat)" risk="CRITICAL" color="#ef4444" />
                        <RiskItem icon={<AlertTriangle size={16} />} label="Ijara (Dengue)" risk="HIGH" color="#8A2BE2" />
                    </div>
                </aside>

            </div>

            <footer style={{ marginTop: '2rem', textAlign: 'center', fontSize: '0.7rem', color: 'var(--text-muted)' }}>
                DESIGNED FOR GARISSA COUNTY | POWERED BY GEMINI ANTIGRAVITY ENGINE
            </footer>
        </div>
    );
};

const NavItem = ({ icon, label, active, onClick }) => (
    <motion.div
        whileHover={{ x: 5 }}
        onClick={onClick}
        className={`nav-item ${active ? 'active' : ''}`}
    >
        {icon} <span>{label}</span>
    </motion.div>
);

const RiskItem = ({ icon, label, risk, color }) => (
    <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', marginBottom: '12px', fontSize: '0.75rem' }}>
        <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
            {icon} <span>{label}</span>
        </div>
        <span style={{ color, fontWeight: 700 }}>{risk}</span>
    </div>
);

export default App;
