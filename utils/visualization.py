"""Visualization utilities for CrewAI examples"""
import time
from datetime import datetime
from typing import List, Optional


def print_section(title: str, content: str = ""):
    """Print a formatted section header"""
    print("\n" + "="*70)
    print(f"  {title}")
    print("="*70)
    if content:
        print(content)
    print()


def print_crew_startup(crew, agents: List, tasks: List, model: str, **config):
    """Print formatted crew startup information"""
    start_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    # Build agents list
    agents_list = "\n".join([
        f"      │ {i+1}. {agent.role[:55]:<55} │"
        for i, agent in enumerate(agents)
    ])
    
    # Build tasks list
    tasks_list = "\n".join([
        f"      │ {i+1}. {task.description[:50]:<50} │"
        for i, task in enumerate(tasks)
    ])
    
    # Build configuration
    config_items = []
    config_items.append(f"      • Process: {config.get('process', 'N/A')}")
    config_items.append(f"      • Model: {model}")
    config_items.append(f"      • Memory: {'Enabled' if config.get('memory', False) else 'Disabled'}")
    config_items.append(f"      • Cache: {'Enabled' if config.get('cache', False) else 'Disabled'}")
    if 'max_rpm' in config:
        config_items.append(f"      • Max RPM: {config['max_rpm']}")
    config_items.append(f"      • Verbose: {config.get('verbose', False)}")
    config_text = "\n".join(config_items)
    
    estimated_time = config.get('estimated_time', '2-5 minutes')
    
    print_section("🚀 CREW EXECUTION STARTING", f"""
      ⏰ Start Time: {start_time}
      
      👥 AGENTS ({len(agents)}):
      ┌─────────────────────────────────────────────────────────┐
{agents_list}
      └─────────────────────────────────────────────────────────┘
      
      📋 TASKS ({len(tasks)}):
      ┌─────────────────────────────────────────────────────────┐
{tasks_list}
      └─────────────────────────────────────────────────────────┘
      
      🔧 CONFIGURATION:
{config_text}
      
      ⚠️  ESTIMATED TIME: {estimated_time}
    """)


def print_execution_start():
    """Print execution start message"""
    print_section("⚙️  EXECUTING CREW", "Watch the agents work in real-time below...\n")


def print_execution_complete(start_time: float, result=None):
    """Print execution completion summary"""
    elapsed_time = time.time() - start_time
    end_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    print_section("✅ EXECUTION COMPLETE", f"""
      ⏰ End Time: {end_time}
      ⏱️  Duration: {elapsed_time:.2f} seconds ({elapsed_time/60:.1f} minutes)
      
      📄 RESULT:
    """)
    
    if result:
        print(result)


def print_outputs_saved(output_files: List[str], output_dir: Optional[str] = None):
    """Print list of saved output files"""
    files_list = "\n".join([f"      ✅ {file}" for file in output_files])
    dir_note = f"\n      📁 All files saved in {output_dir}/" if output_dir else ""
    
    print_section("📁 OUTPUTS SAVED", f"""
{files_list}{dir_note}
    """)


def create_timer():
    """Create and return a timer function"""
    start = time.time()
    return lambda: time.time() - start

