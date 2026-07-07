import pandas as pd
import numpy as np

def generate_sample_dataset(filename='raw_data.csv', rows=1000):
    np.random.seed(42)
    
    data = {
        'age': np.random.randint(18, 80, rows),
        'salary': np.random.normal(50000, 15000, rows),
        'experience': np.random.randint(0, 40, rows),
        'score': np.random.uniform(0, 100, rows),
        'department': np.random.choice(['Sales', 'IT', 'HR', 'Finance', 'Marketing'], rows),
        'performance': np.random.choice(['Low', 'Medium', 'High'], rows)
    }
    
    df = pd.DataFrame(data)
    
    missing_indices_age = np.random.choice(df.index, size=int(0.05*len(df)), replace=False)
    df.loc[missing_indices_age, 'salary'] = np.nan
    
    missing_indices_score = np.random.choice(df.index, size=int(0.03*len(df)), replace=False)
    df.loc[missing_indices_score, 'score'] = np.nan
    
    outlier_indices = np.random.choice(df.index, size=int(0.02*len(df)), replace=False)
    df.loc[outlier_indices, 'salary'] = np.random.choice([150000, -10000], size=len(outlier_indices))
    
    duplicate_rows = df.sample(n=20, random_state=42)
    df = pd.concat([df, duplicate_rows], ignore_index=True)
    
    df = df.sample(frac=1).reset_index(drop=True)
    
    df.to_csv(filename, index=False)
    print(f"Sample dataset generated: {filename} ({len(df)} rows)")
    return df

if __name__ == "__main__":
    generate_sample_dataset()
