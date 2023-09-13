/**
 * @param {string[]} emails
 * @return {number}
 */
var numUniqueEmails = function(emails) {
    /*
    
    */
    
    let uniqueEmail = new Set();
    for(let email of emails){
        let [local, domain] = email.split('@');
        local = local.replace(/\./g, '');
        
        let plusIdx = local.indexOf('+');
        if(plusIdx !== -1){
            local = local.substring(0,plusIdx);
        }
        uniqueEmail.add(local + '@' + domain)
    }
    return uniqueEmail.size
};