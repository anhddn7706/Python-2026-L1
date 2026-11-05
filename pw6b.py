import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('scores.csv')

df['math'] = pd.to_numeric(df['math'], errors='coerce')
df['python'] = pd.to_numeric(df['python'], errors='coerce')
df['db'] = pd.to_numeric(df['db'], errors='coerce')

plt.figure()

x = range(len(df))

plt.scatter(x, df['math'], color='blue', label='Math')
plt.scatter(x, df['python'], color='green', label='Python')
plt.scatter(x, df['db'], color='red', label='DB')

plt.title('Student Scores (Scatter Plot)')
plt.xlabel('Student Index')
plt.ylabel('Scores')
plt.legend()

plt.savefig('scattered.png')
plt.show()

plt.subplot(1, 3, 1)
plt.hist(df['math'].dropna(), color='blue')
plt.title('Math')
plt.xlabel('Marks')
plt.ylabel('Frequency')

plt.subplot(1, 3, 2)
plt.hist(df['python'].dropna(), color='green')
plt.title('Python')
plt.xlabel('Marks')

plt.subplot(1, 3, 3)
plt.hist(df['db'].dropna(), color='red')
plt.title('DB')
plt.xlabel('Marks')

plt.tight_layout()

plt.savefig('histo.png')
plt.show()

plt.figure()

df[['math', 'python', 'db']].boxplot()

plt.title('Box Plot of Course Marks')
plt.ylabel('Marks')

plt.savefig('box.png')
plt.show()