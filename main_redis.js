// ## test local install
// docker run -it --name redis-stack -p 6379:6379 redis/redis-stack-server:latest
// npm install redis
// node main_redis.js

const { createClient } = await import("redis");

const client =createClient({ url: 'redis://redis:6379' });

client.on('error', err => console.log('Redis Client Error', err));
await client.connect();
await client.set('key1', 'value1');
const value = await client.get('key1');
console.log("value: "+value);


const data = {
  user: {
    name: 'Alice',
    age: 30,
    skills: ['Python', 'Redis']
  }
};

await client.json.set('user_1', '$', data);

console.log(await client.json.get('user_1'));

console.log(await client.json.get('user_1', { path: '.user.name' }));

await client.json.set('user_1', '.user.age', 31);
console.log(await client.json.get('user_1'));


await client.json.set('user_1', '.user', {
  name: 'Lihi',
  age: 19,
  skills: ['Python', 'Redis', 'JS']
});

let skills = await client.json.get('user_1', { path: '.user.skills' });
skills.push('ubuntu');
await client.json.set('user_1', '.user.skills', skills);

await client.json.arrAppend('user_1', '.user.skills', 'driving');

await client.json.arrInsert('user_1', '.user.skills', 1, 'swimming');

await client.json.set('user_1', '.user.friends', []);

await client.json.clear('user_1');

await client.json.del('user_1', '.user.age');

await client.json.set('user_1', '$', data);

await client.json.merge('user_1', '$', { user2: { playing: true } });

await client.json.numIncrBy('user_1', '.user.age', 1);

console.log(await client.json.objLen('user_1', '.user'));

console.log("current data:",await client.json.get('user_1'));
console.log("current .user.skills: ",await client.json.get("user_1", { path: '.user.skills' }));

console.log(await client.json.arrLen('user_1', { path: '.user.skills' }));

console.log(await client.json.objKeys('user_1', { path: '.user' }));

console.log(await client.json.strLen('user_1', { path: '.user.name' }));

console.log(await client.json.get('user_1', { path: '.user.name' }));

console.log(await client.json.get('user_1'));

// await client.json.strAppend('user_1', '$.user.name', 'lihi');
console.log("done");

await client.quit();


