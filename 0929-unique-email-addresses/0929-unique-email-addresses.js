/**
 * @param {string[]} emails
 * @return {number}
 */
var numUniqueEmails = function(emails) {
    /*
    1. separated by @
    local + @ + domain
    
    2. if '.' in local, just ignore. 
    
    3. if '+' in local, after the sign, ignore the next letters 
    */
     let set = new Set();
    
    for(const email of emails){
        const [local, domain] = email.split('@');
    
   
    
    const removeDot = local.replace(/\./g, '');
    const findPlus = removeDot.indexOf('+');
    const validLocal = findPlus === -1 ? removeDot : removeDot.substring(0, findPlus);
    
    const validEmail = validLocal + '@' + domain;
    
    set.add(validEmail);
    }
    
    
    return set.size
};